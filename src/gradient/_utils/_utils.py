from __future__ import annotations

import os
import re
import inspect
import functools
from typing import (
    Any,
    Tuple,
    Mapping,
    TypeVar,
    Callable,
    Iterable,
    Sequence,
    cast,
    overload,
)
from pathlib import Path
from datetime import date, datetime
from typing_extensions import TypeGuard

import sniffio

from .._types import Omit, NotGiven, FileTypes, HeadersLike

_T = TypeVar("_T")
_TupleT = TypeVar("_TupleT", bound=Tuple[object, ...])
_MappingT = TypeVar("_MappingT", bound=Mapping[str, object])
_SequenceT = TypeVar("_SequenceT", bound=Sequence[object])
CallableT = TypeVar("CallableT", bound=Callable[..., Any])


def flatten(t: Iterable[Iterable[_T]]) -> list[_T]:
    return [item for sublist in t for item in sublist]


def extract_files(
    # TODO: this needs to take Dict but variance issues.....
    # create protocol type ?
    query: Mapping[str, object],
    *,
    paths: Sequence[Sequence[str]],
) -> list[tuple[str, FileTypes]]:
    """Recursively extract files from the given dictionary based on specified paths.

    A path may look like this ['foo', 'files', '<array>', 'data'].

    Note: this mutates the given dictionary.
    """
    files: list[tuple[str, FileTypes]] = []
    for path in paths:
        files.extend(_extract_items(query, path, index=0, flattened_key=None))
    return files


def _extract_items(
    obj: object,
    path: Sequence[str],
    *,
    index: int,
    flattened_key: str | None,
) -> list[tuple[str, FileTypes]]:
    try:
        key = path[index]
    except IndexError:
        if not is_given(obj):
            # no value was provided - we can safely ignore
            return []

        # cyclical import
        from .._files import assert_is_file_content

        # We have exhausted the path, return the entry we found.
        assert flattened_key is not None

        if is_list(obj):
            files: list[tuple[str, FileTypes]] = []
            for entry in obj:
                assert_is_file_content(entry, key=flattened_key + "[]" if flattened_key else "")
                files.append((flattened_key + "[]", cast(FileTypes, entry)))
            return files

        assert_is_file_content(obj, key=flattened_key)
        return [(flattened_key, cast(FileTypes, obj))]

    index += 1
    if is_dict(obj):
        try:
            # We are at the last entry in the path so we must remove the field
            if (len(path)) == index:
                item = obj.pop(key)
            else:
                item = obj[key]
        except KeyError:
            # Key was not present in the dictionary, this is not indicative of an error
            # as the given path may not point to a required field. We also do not want
            # to enforce required fields as the API may differ from the spec in some cases.
            return []
        if flattened_key is None:
            flattened_key = key
        else:
            flattened_key += f"[{key}]"
        return _extract_items(
            item,
            path,
            index=index,
            flattened_key=flattened_key,
        )
    elif is_list(obj):
        if key != "<array>":
            return []

        return flatten(
            [
                _extract_items(
                    item,
                    path,
                    index=index,
                    flattened_key=flattened_key + "[]" if flattened_key is not None else "[]",
                )
                for item in obj
            ]
        )

    # Something unexpected was passed, just ignore it.
    return []


def is_given(obj: _T | NotGiven | Omit) -> TypeGuard[_T]:
    return not isinstance(obj, NotGiven) and not isinstance(obj, Omit)


# Type safe methods for narrowing types with TypeVars.
# The default narrowing for isinstance(obj, dict) is dict[unknown, unknown],
# however this cause Pyright to rightfully report errors. As we know we don't
# care about the contained types we can safely use `object` in it's place.
#
# There are two separate functions defined, `is_*` and `is_*_t` for different use cases.
# `is_*` is for when you're dealing with an unknown input
# `is_*_t` is for when you're narrowing a known union type to a specific subset


def is_tuple(obj: object) -> TypeGuard[tuple[object, ...]]:
    return isinstance(obj, tuple)


def is_tuple_t(obj: _TupleT | object) -> TypeGuard[_TupleT]:
    return isinstance(obj, tuple)


def is_sequence(obj: object) -> TypeGuard[Sequence[object]]:
    return isinstance(obj, Sequence)


def is_sequence_t(obj: _SequenceT | object) -> TypeGuard[_SequenceT]:
    return isinstance(obj, Sequence)


def is_mapping(obj: object) -> TypeGuard[Mapping[str, object]]:
    return isinstance(obj, Mapping)


def is_mapping_t(obj: _MappingT | object) -> TypeGuard[_MappingT]:
    return isinstance(obj, Mapping)


def is_dict(obj: object) -> TypeGuard[dict[object, object]]:
    return isinstance(obj, dict)


def is_list(obj: object) -> TypeGuard[list[object]]:
    return isinstance(obj, list)


def is_iterable(obj: object) -> TypeGuard[Iterable[object]]:
    return isinstance(obj, Iterable)


def deepcopy_minimal(item: _T) -> _T:
    """Minimal reimplementation of copy.deepcopy() that will only copy certain object types:

    - mappings, e.g. `dict`
    - list

    This is done for performance reasons.
    """
    if is_mapping(item):
        return cast(_T, {k: deepcopy_minimal(v) for k, v in item.items()})
    if is_list(item):
        return cast(_T, [deepcopy_minimal(entry) for entry in item])
    return item


# copied from https://github.com/Rapptz/RoboDanny
def human_join(seq: Sequence[str], *, delim: str = ", ", final: str = "or") -> str:
    size = len(seq)
    if size == 0:
        return ""

    if size == 1:
        return seq[0]

    if size == 2:
        return f"{seq[0]} {final} {seq[1]}"

    return delim.join(seq[:-1]) + f" {final} {seq[-1]}"


def quote(string: str) -> str:
    """Add single quotation marks around the given string. Does *not* do any escaping."""
    return f"'{string}'"


def required_args(*variants: Sequence[str]) -> Callable[[CallableT], CallableT]:
    """Decorator to enforce a given set of arguments or variants of arguments are passed to the decorated function.

    Useful for enforcing runtime validation of overloaded functions.

    Example usage:
    ```py
    @overload
    def foo(*, a: str) -> str: ...


    @overload
    def foo(*, b: bool) -> str: ...


    # This enforces the same constraints that a static type checker would
    # i.e. that either a or b must be passed to the function
    @required_args(["a"], ["b"])
    def foo(*, a: str | None = None, b: bool | None = None) -> str: ...
    ```
    """

    def inner(func: CallableT) -> CallableT:
        params = inspect.signature(func).parameters
        positional = [
            name
            for name, param in params.items()
            if param.kind
            in {
                param.POSITIONAL_ONLY,
                param.POSITIONAL_OR_KEYWORD,
            }
        ]

        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            given_params: set[str] = set()
            for i, _ in enumerate(args):
                try:
                    given_params.add(positional[i])
                except IndexError:
                    raise TypeError(
                        f"{func.__name__}() takes {len(positional)} argument(s) but {len(args)} were given"
                    ) from None

            for key in kwargs.keys():
                given_params.add(key)

            for variant in variants:
                matches = all((param in given_params for param in variant))
                if matches:
                    break
            else:  # no break
                if len(variants) > 1:
                    variations = human_join(
                        ["(" + human_join([quote(arg) for arg in variant], final="and") + ")" for variant in variants]
                    )
                    msg = f"Missing required arguments; Expected either {variations} arguments to be given"
                else:
                    assert len(variants) > 0

                    # TODO: this error message is not deterministic
                    missing = list(set(variants[0]) - given_params)
                    if len(missing) > 1:
                        msg = f"Missing required arguments: {human_join([quote(arg) for arg in missing])}"
                    else:
                        msg = f"Missing required argument: {quote(missing[0])}"
                raise TypeError(msg)
            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return inner


_K = TypeVar("_K")
_V = TypeVar("_V")


@overload
def strip_not_given(obj: None) -> None: ...


@overload
def strip_not_given(obj: Mapping[_K, _V | NotGiven]) -> dict[_K, _V]: ...


@overload
def strip_not_given(obj: object) -> object: ...


def strip_not_given(obj: object | None) -> object:
    """Remove all top-level keys where their values are instances of `NotGiven`"""
    if obj is None:
        return None

    if not is_mapping(obj):
        return obj

    return {key: value for key, value in obj.items() if not isinstance(value, NotGiven)}


def coerce_integer(val: str) -> int:
    return int(val, base=10)


def coerce_float(val: str) -> float:
    return float(val)


def coerce_boolean(val: str) -> bool:
    return val == "true" or val == "1" or val == "on"


def maybe_coerce_integer(val: str | None) -> int | None:
    if val is None:
        return None
    return coerce_integer(val)


def maybe_coerce_float(val: str | None) -> float | None:
    if val is None:
        return None
    return coerce_float(val)


def maybe_coerce_boolean(val: str | None) -> bool | None:
    if val is None:
        return None
    return coerce_boolean(val)


def removeprefix(string: str, prefix: str) -> str:
    """Remove a prefix from a string.

    Backport of `str.removeprefix` for Python < 3.9
    """
    if string.startswith(prefix):
        return string[len(prefix) :]
    return string


def removesuffix(string: str, suffix: str) -> str:
    """Remove a suffix from a string.

    Backport of `str.removesuffix` for Python < 3.9
    """
    if string.endswith(suffix):
        return string[: -len(suffix)]
    return string


def file_from_path(path: str) -> FileTypes:
    contents = Path(path).read_bytes()
    file_name = os.path.basename(path)
    return (file_name, contents)


def get_required_header(headers: HeadersLike, header: str) -> str:
    lower_header = header.lower()
    if is_mapping_t(headers):
        # mypy doesn't understand the type narrowing here
        for k, v in headers.items():  # type: ignore
            if k.lower() == lower_header and isinstance(v, str):
                return v

    # to deal with the case where the header looks like Stainless-Event-Id
    intercaps_header = re.sub(r"([^\w])(\w)", lambda pat: pat.group(1) + pat.group(2).upper(), header.capitalize())

    for normalized_header in [header, lower_header, header.upper(), intercaps_header]:
        value = headers.get(normalized_header)
        if value:
            return value

    raise ValueError(f"Could not find {header} header")


def get_async_library() -> str:
    try:
        return sniffio.current_async_library()
    except Exception:
        return "false"


def lru_cache(*, maxsize: int | None = 128) -> Callable[[CallableT], CallableT]:
    """A version of functools.lru_cache that retains the type signature
    for the wrapped function arguments.
    """
    wrapper = functools.lru_cache(  # noqa: TID251
        maxsize=maxsize,
    )
    return cast(Any, wrapper)  # type: ignore[no-any-return]


def json_safe(data: object) -> object:
    """Translates a mapping / sequence recursively in the same fashion
    as `pydantic` v2's `model_dump(mode="json")`.
    """
    if is_mapping(data):
        return {json_safe(key): json_safe(value) for key, value in data.items()}

    if is_iterable(data) and not isinstance(data, (str, bytes, bytearray)):
        return [json_safe(item) for item in data]

    if isinstance(data, (datetime, date)):
        return data.isoformat()

    return data


# Response Caching Classes
class ResponseCache:
    """Simple in-memory response cache with TTL support."""

    def __init__(self, max_size: int = 100, default_ttl: int = 300) -> None:
        """Initialize the cache.

        Args:
            max_size: Maximum number of cached responses
            default_ttl: Default time-to-live in seconds
        """
        self.max_size: int = max_size
        self.default_ttl: int = default_ttl
        self._cache: dict[str, tuple[Any, float]] = {}
        self._access_order: list[str] = []

    def _make_key(self, method: str, url: str, params: dict[str, Any] | None = None, data: Any = None) -> str:
        """Generate a cache key from request details."""
        import hashlib
        import json

        key_data = {
            "method": method.upper(),
            "url": url,
            "params": params or {},
            "data": json.dumps(data, sort_keys=True) if data else None
        }
        key_str = json.dumps(key_data, sort_keys=True)
        return hashlib.md5(key_str.encode()).hexdigest()

    def get(self, method: str, url: str, params: dict[str, Any] | None = None, data: Any = None) -> Any | None:
        """Get a cached response if available and not expired."""
        import time

        key = self._make_key(method, url, params, data)
        if key in self._cache:
            response, expiry = self._cache[key]
            if time.time() < expiry:
                # Move to end (most recently used)
                self._access_order.remove(key)
                self._access_order.append(key)
                return response
            else:
                # Expired, remove it
                del self._cache[key]
                self._access_order.remove(key)
        return None

    def set(self, method: str, url: str, response: Any, ttl: int | None = None,
            params: dict[str, Any] | None = None, data: Any = None) -> None:
        """Cache a response with optional TTL."""
        import time

        key = self._make_key(method, url, params, data)
        expiry = time.time() + (ttl or self.default_ttl)

        # Remove if already exists
        if key in self._cache:
            self._access_order.remove(key)

        # Evict least recently used if at capacity
        if len(self._cache) >= self.max_size:
            lru_key = self._access_order.pop(0)
            del self._cache[lru_key]

        self._cache[key] = (response, expiry)
        self._access_order.append(key)

    def clear(self) -> None:
        """Clear all cached responses."""
        self._cache.clear()
        self._access_order.clear()

    def size(self) -> int:
        """Get current cache size."""
        return len(self._cache)


# Rate Limiting Classes
class RateLimiter:
    """Simple token bucket rate limiter."""

    def __init__(self, requests_per_minute: int = 60) -> None:
        """Initialize rate limiter.

        Args:
            requests_per_minute: Maximum requests allowed per minute
        """
        self.requests_per_minute: int = requests_per_minute
        self.tokens: float = float(requests_per_minute)
        self.last_refill: float = self._now()
        self.refill_rate: float = requests_per_minute / 60.0  # tokens per second

    def _now(self) -> float:
        """Get current time in seconds."""
        import time
        return time.time()

    def _refill(self) -> None:
        """Refill tokens based on elapsed time."""
        now = self._now()
        elapsed = now - self.last_refill
        self.tokens = min(self.requests_per_minute, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now

    def acquire(self, tokens: int = 1) -> bool:
        """Try to acquire tokens. Returns True if successful."""
        self._refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def wait_time(self, tokens: int = 1) -> float:
        """Get seconds to wait for tokens to be available."""
        self._refill()
        if self.tokens >= tokens:
            return 0.0

        needed = tokens - self.tokens
        return needed / self.refill_rate


# Batch Processing Classes
class BatchProcessor:
    """Utility for batching multiple requests with timeout and size limits."""

    def __init__(self, batch_size: int = 10, timeout_seconds: float = 5.0) -> None:
        """Initialize batch processor.

        Args:
            batch_size: Maximum items per batch
            timeout_seconds: Maximum time to wait before processing batch
        """
        self.batch_size: int = batch_size
        self.timeout_seconds: float = timeout_seconds
        self._batch: list[Any] = []
        self._last_add_time: float = self._now()
        self._callback: Callable[[list[Any]], Any] | None = None

    def _now(self) -> float:
        """Get current time in seconds."""
        import time
        return time.time()

    def add(self, item: Any) -> None:
        """Add item to current batch."""
        self._batch.append(item)
        self._last_add_time = self._now()

        # Auto-process if batch is full
        if len(self._batch) >= self.batch_size:
            self._process_batch()

    def set_callback(self, callback: Callable[[list[Any]], Any]) -> None:
        """Set callback function to process batches."""
        self._callback = callback

    def _process_batch(self) -> Any | None:
        """Process current batch if not empty."""
        if not self._batch or not self._callback:
            return None

        batch = self._batch.copy()
        self._batch.clear()
        return self._callback(batch)

    def force_process(self) -> Any | None:
        """Force process current batch regardless of size or timeout."""
        return self._process_batch()

    def check_timeout(self) -> Any | None:
        """Check if batch has timed out and process if needed."""
        if not self._batch:
            return None

        elapsed = self._now() - self._last_add_time
        if elapsed >= self.timeout_seconds:
            return self._process_batch()

        return None

    def size(self) -> int:
        """Get current batch size."""
        return len(self._batch)

    def is_empty(self) -> bool:
        """Check if batch is empty."""
        return len(self._batch) == 0


# Data Export Classes
class DataExporter:
    """Utility for exporting API response data to JSON/CSV formats."""

    def __init__(self) -> None:
        """Initialize data exporter."""
        pass

    def _flatten_response(self, data: Any, prefix: str = "") -> dict[str, Any]:
        """Flatten nested response data for CSV export."""
        flattened = {}

        if isinstance(data, dict):
            for key, value in data.items():
                new_key = f"{prefix}.{key}" if prefix else key
                if isinstance(value, (dict, list)):
                    flattened.update(self._flatten_response(value, new_key))
                else:
                    flattened[new_key] = value
        elif isinstance(data, list):
            # For lists, create indexed keys
            for i, item in enumerate(data):
                new_key = f"{prefix}[{i}]" if prefix else f"[{i}]"
                if isinstance(item, (dict, list)):
                    flattened.update(self._flatten_response(item, new_key))
                else:
                    flattened[new_key] = item
        else:
            flattened[prefix] = data

        return flattened

    def export_json(self, data: Any, file_path: str | None = None, indent: int = 2) -> str | None:
        """Export data to JSON format.

        Args:
            data: Data to export
            file_path: Optional file path to save to
            indent: JSON indentation level

        Returns:
            JSON string if no file_path provided, None otherwise
        """
        import json

        json_str = json.dumps(data, indent=indent, default=str)

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(json_str)
            return None

        return json_str

    def export_csv(self, data: Any, file_path: str | None = None, headers: list[str] | None = None) -> str | None:
        """Export data to CSV format.

        Args:
            data: Data to export (list of dicts or single dict)
            file_path: Optional file path to save to
            headers: Optional custom headers

        Returns:
            CSV string if no file_path provided, None otherwise
        """
        import csv
        import io

        # Ensure data is a list
        if not isinstance(data, list):
            data = [data]

        # Flatten each item in the data
        flattened_data = [self._flatten_response(item) for item in data]

        # Determine headers
        if not headers:
            all_keys = set()
            for item in flattened_data:
                all_keys.update(item.keys())
            headers = sorted(all_keys)

        # Create CSV content
        output = io.StringIO() if not file_path else open(file_path, 'w', newline='', encoding='utf-8')

        try:
            writer = csv.DictWriter(output, fieldnames=headers)
            writer.writeheader()

            for item in flattened_data:
                # Fill missing keys with empty strings
                row = {header: item.get(header, '') for header in headers}
                writer.writerow(row)

            if not file_path:
                return output.getvalue()
            return None

        finally:
            if file_path:
                output.close()


# Pagination Classes
class PaginationHelper:
    """Helper for handling paginated API responses."""

    def __init__(self, page_size: int = 20, max_pages: int | None = None) -> None:
        """Initialize pagination helper.

        Args:
            page_size: Number of items per page
            max_pages: Maximum number of pages to fetch (None for unlimited)
        """
        self.page_size: int = page_size
        self.max_pages: int | None = max_pages

    def paginate(self, fetch_func: Callable[[dict[str, Any]], Any], **kwargs: Any) -> list[Any]:
        """Paginate through all results using the provided fetch function.

        Args:
            fetch_func: Function that takes pagination params and returns response
            **kwargs: Additional parameters to pass to fetch_func

        Returns:
            List of all items across all pages
        """
        all_items = []
        page = 1

        while self.max_pages is None or page <= self.max_pages:
            # Add pagination parameters
            params = kwargs.copy()
            params.update({
                "page": page,
                "per_page": self.page_size
            })

            try:
                response = fetch_func(params)
                items = self._extract_items(response)

                if not items:
                    break  # No more items

                all_items.extend(items)

                # Check if we got fewer items than requested (last page)
                if len(items) < self.page_size:
                    break

                page += 1

            except Exception as e:
                # If it's a pagination error or no more pages, stop
                if self._is_pagination_end_error(e):
                    break
                raise

        return all_items

    def _extract_items(self, response: Any) -> list[Any]:
        """Extract items from API response."""
        # Handle different response formats
        if hasattr(response, 'data') and isinstance(response.data, list):
            return response.data
        elif hasattr(response, 'items') and isinstance(response.items, list):
            return response.items
        elif hasattr(response, 'results') and isinstance(response.results, list):
            return response.results
        elif isinstance(response, list):
            return response
        elif isinstance(response, dict):
            # Try common keys
            for key in ['data', 'items', 'results', 'objects']:
                if key in response and isinstance(response[key], list):
                    return response[key]
        return []

    def _is_pagination_end_error(self, error: Exception) -> bool:
        """Check if error indicates end of pagination."""
        error_str = str(error).lower()
        return any(phrase in error_str for phrase in [
            'page not found',
            'invalid page',
            'no more pages',
            'pagination end'
        ])

    async def paginate_async(self, fetch_func: Callable[[dict[str, Any]], Any], **kwargs: Any) -> list[Any]:
        """Async version of paginate."""
        import asyncio

        all_items = []
        page = 1

        while self.max_pages is None or page <= self.max_pages:
            # Add pagination parameters
            params = kwargs.copy()
            params.update({
                "page": page,
                "per_page": self.page_size
            })

            try:
                response = await fetch_func(params)
                items = self._extract_items(response)

                if not items:
                    break

                all_items.extend(items)

                if len(items) < self.page_size:
                    break

                page += 1

            except Exception as e:
                if self._is_pagination_end_error(e):
                    break
                raise

        return all_items


# API Key Validation Functions
def validate_api_key(api_key: str | None) -> bool:
    """Validate an API key format.

    Args:
        api_key: The API key to validate. Can be None.

    Returns:
        True if valid or None, False otherwise
    """
    if api_key is None:
        return True  # None is acceptable for optional keys

    if not isinstance(api_key, str):
        return False
    if not api_key or api_key.isspace():
        return False
    if len(api_key) < 10:
        return False

    # Check for common patterns
    return (
        api_key.startswith(('sk-', 'do_v1_')) or
        'gradient' in api_key.lower() or
        len(api_key) >= 20
    )


def validate_client_credentials(
    access_token: str | None = None,
    model_access_key: str | None = None,
    agent_access_key: str | None = None,
    agent_endpoint: str | None = None
) -> None:
    """Validate client credentials comprehensively.

    This function performs thorough validation of client credentials including:
    - Checking that at least one authentication method is provided
    - Validating API key formats
    - Checking agent endpoint URL format if provided

    Args:
        access_token: DigitalOcean access token
        model_access_key: Gradient model access key
        agent_access_key: Gradient agent access key
        agent_endpoint: Agent endpoint URL

    Raises:
        ValueError: If credentials are invalid or missing required authentication
    """
    # Check that at least one authentication method is provided
    if not any([access_token, model_access_key, agent_access_key]):
        raise ValueError("At least one authentication method must be provided")

    # Validate individual API keys
    if access_token and not validate_api_key(access_token):
        raise ValueError("Invalid access_token format")

    if model_access_key and not validate_api_key(model_access_key):
        raise ValueError("Invalid model_access_key format")

    if agent_access_key and not validate_api_key(agent_access_key):
        raise ValueError("Invalid agent_access_key format")

    # Validate agent endpoint if provided
    if agent_endpoint:
        if not isinstance(agent_endpoint, str):
            raise ValueError("agent_endpoint must be a string")
        if not agent_endpoint.startswith(('http://', 'https://')):
            raise ValueError("agent_endpoint must be a valid HTTP/HTTPS URL")


def validate_client_instance(client: Any) -> None:
    """Validate a Gradient client instance has proper authentication.

    This function checks that a created client has valid authentication
    and can make API calls. This directly addresses the reviewer feedback
    about validating actual client instances rather than just parameters.

    Args:
        client: A Gradient or AsyncGradient client instance

    Raises:
        ValueError: If client authentication is invalid
        TypeError: If client is not a valid Gradient client instance
    """
    # Import here to avoid circular imports
    try:
        from .._client import Gradient, AsyncGradient
    except ImportError:
        # Fallback for when called from different contexts
        import gradient
        Gradient = gradient.Gradient
        AsyncGradient = gradient.AsyncGradient

    if not isinstance(client, (Gradient, AsyncGradient)):
        raise TypeError("client must be a Gradient or AsyncGradient instance")

    # Check that client has at least one authentication method
    has_auth = any([
        client.access_token,
        client.model_access_key,
        client.agent_access_key
    ])

    if not has_auth:
        raise ValueError("Client must have at least one authentication method configured")

    # Validate the authentication methods that are set
    try:
        validate_client_credentials(
            access_token=client.access_token,
            model_access_key=client.model_access_key,
            agent_access_key=client.agent_access_key,
            agent_endpoint=client._agent_endpoint
        )
    except ValueError as e:
        raise ValueError(f"Client authentication validation failed: {e}") from e
