from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, Generic, TypeVar, Callable, cast, overload
from datetime import date, datetime
from typing_extensions import Self, Literal

import pydantic
from pydantic.fields import FieldInfo

from ._types import IncEx, StrBytesIntFloat

_T = TypeVar("_T")
_ModelT = TypeVar("_ModelT", bound=pydantic.BaseModel)

# --------------- Pydantic v2, v3 compatibility ---------------

PYDANTIC_V1 = pydantic.VERSION.startswith("1.")

if TYPE_CHECKING:

    def parse_date(value: date | StrBytesIntFloat) -> date: ...
    def parse_datetime(value: Union[datetime, StrBytesIntFloat]) -> datetime: ...
    def get_args(t: type[Any]) -> tuple[Any, ...]: ...
    def is_union(tp: type[Any] | None) -> bool: ...
    def get_origin(t: type[Any]) -> type[Any] | None: ...
    def is_literal_type(type_: type[Any]) -> bool: ...
    def is_typeddict(type_: type[Any]) -> bool: ...

else:
    if PYDANTIC_V1:
        # Pydantic v1 re-exports
        from pydantic.typing import (
            get_args,
            is_union,
            get_origin,
            is_typeddict,
            is_literal_type,
        )
        from pydantic.datetime_parse import parse_date, parse_datetime
    else:
        # Safe fallback import — avoids crash if _utils missing
        try:
            from ._utils import (
                get_args,
                is_union,
                get_origin,
                parse_date,
                is_typeddict,
                parse_datetime,
                is_literal_type,
            )
        except ModuleNotFoundError:
            # fallback to pydantic builtins if _utils missing
            from pydantic import TypeAdapter
            def get_args(t: Any) -> tuple[Any, ...]: return getattr(t, "__args__", ())
            def get_origin(t: Any) -> Any: return getattr(t, "__origin__", None)
            def parse_date(value): return TypeAdapter(date).validate_python(value)
            def parse_datetime(value): return TypeAdapter(datetime).validate_python(value)
            def is_union(tp): return getattr(tp, "__origin__", None) is Union
            def is_literal_type(t): return getattr(t, "__origin__", None).__name__ == "Literal"
            def is_typeddict(t): return hasattr(t, "__annotations__")


# ---------------- ConfigDict handling ----------------
if TYPE_CHECKING:
    from pydantic import ConfigDict
else:
    if PYDANTIC_V1:
        ConfigDict = None
    else:
        from pydantic import ConfigDict


# ---------------- Core compatibility helpers ----------------

def parse_obj(model: type[_ModelT], value: object) -> _ModelT:
    if PYDANTIC_V1:
        return cast(_ModelT, model.parse_obj(value))
    return model.model_validate(value)


def field_is_required(field: FieldInfo) -> bool:
    if PYDANTIC_V1:
        return field.required  # type: ignore
    return field.is_required()


def field_get_default(field: FieldInfo) -> Any:
    value = field.get_default()
    if PYDANTIC_V1:
        return value
    from pydantic_core import PydanticUndefined
    return None if value == PydanticUndefined else value


def field_outer_type(field: FieldInfo) -> Any:
    return field.outer_type_ if PYDANTIC_V1 else field.annotation


def get_model_config(model: type[pydantic.BaseModel]) -> Any:
    return model.__config__ if PYDANTIC_V1 else model.model_config


def get_model_fields(model: type[pydantic.BaseModel]) -> dict[str, FieldInfo]:
    return model.__fields__ if PYDANTIC_V1 else model.model_fields


def model_copy(model: _ModelT, *, deep: bool = False) -> _ModelT:
    return model.copy(deep=deep) if PYDANTIC_V1 else model.model_copy(deep=deep)


def model_json(model: pydantic.BaseModel, *, indent: int | None = None) -> str:
    return model.json(indent=indent) if PYDANTIC_V1 else model.model_dump_json(indent=indent)


def model_dump(
    model: pydantic.BaseModel,
    *,
    exclude: IncEx | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    warnings: bool = True,
    mode: Literal["json", "python"] = "python",
) -> dict[str, Any]:
    if hasattr(model, "model_dump"):  # Pydantic v2+
        return model.model_dump(
            mode=mode,
            exclude=exclude,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            warnings=warnings,
        )
    # Pydantic v1 fallback
    return cast(
        "dict[str, Any]",
        model.dict(
            exclude=exclude,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
        ),
    )


def model_parse(model: type[_ModelT], data: Any) -> _ModelT:
    return model.parse_obj(data) if PYDANTIC_V1 else model.model_validate(data)


# ---------------- GenericModel compatibility ----------------
if TYPE_CHECKING:

    class GenericModel(pydantic.BaseModel): ...
else:
    if PYDANTIC_V1:
        import pydantic.generics
        class GenericModel(pydantic.generics.GenericModel, pydantic.BaseModel): ...
    else:
        class GenericModel(pydantic.BaseModel): ...


# ---------------- cached_property handling ----------------
if TYPE_CHECKING:
    cached_property = property

    class typed_cached_property(Generic[_T]):
        func: Callable[[Any], _T]
        attrname: str | None

        def __init__(self, func: Callable[[Any], _T]) -> None: ...
        @overload
        def __get__(self, instance: None, owner: type[Any] | None = None) -> Self: ...
        @overload
        def __get__(self, instance: object, owner: type[Any] | None = None) -> _T: ...
        def __get__(self, instance: object, owner: type[Any] | None = None) -> _T | Self:
            raise NotImplementedError()
        def __set_name__(self, owner: type[Any], name: str) -> None: ...
        def __set__(self, instance: object, value: _T) -> None: ...
else:
    from functools import cached_property as cached_property
    typed_cached_property = cached_property
