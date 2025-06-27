from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `do_gradientai.resources` module.

    This is used so that we can lazily import `do_gradientai.resources` only when
    needed *and* so that users can just import `do_gradientai` and reference `do_gradientai.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("do_gradientai.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
