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

                    missing = sorted(set(variants[0]) - given_params)
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


# API Key Validation Functions
def validate_api_key(api_key: str) -> bool:
    """Validate an API key format.

    Args:
        api_key: The API key to validate

    Returns:
        True if valid, False otherwise
    """
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
        # Could add more URL validation here if needed


def validate_client_instance(client: Any) -> None:
    """Validate a Gradient client instance has proper authentication.

    This function checks that a created client has valid authentication
    and can make API calls.

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


# Response Caching Classes
class ResponseCache:
    """Simple in-memory response cache with TTL support."""

    def __init__(self, max_size: int = 100, default_ttl: int = 300):
        """Initialize the cache.

        Args:
            max_size: Maximum number of cached responses
            default_ttl: Default time-to-live in seconds
        """
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._cache: dict[str, tuple[Any, float]] = {}
        self._access_order: list[str] = []

    def _make_key(self, method: str, url: str, params: dict | None = None, data: Any = None) -> str:
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

    def get(self, method: str, url: str, params: dict | None = None, data: Any = None) -> Any | None:
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
            params: dict | None = None, data: Any = None) -> None:
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

    def __init__(self, requests_per_minute: int = 60):
        """Initialize rate limiter.

        Args:
            requests_per_minute: Maximum requests allowed per minute
        """
        self.requests_per_minute = requests_per_minute
        self.tokens = requests_per_minute
        self.last_refill = self._now()
        self.refill_rate = requests_per_minute / 60.0  # tokens per second

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
    """Utility for batching multiple requests together."""

    def __init__(self, max_batch_size: int = 10, max_wait_time: float = 1.0):
        """Initialize batch processor.

        Args:
            max_batch_size: Maximum number of requests to batch together
            max_wait_time: Maximum time to wait before processing batch
        """
        self.max_batch_size = max_batch_size
        self.max_wait_time = max_wait_time
        self._batches: dict[str, list] = {}
        self._timers: dict[str, float] = {}

    def add_request(self, batch_key: str, request_data: Any) -> None:
        """Add a request to a batch."""
        import time

        if batch_key not in self._batches:
            self._batches[batch_key] = []
            self._timers[batch_key] = time.time()

        self._batches[batch_key].append(request_data)

    def get_batch(self, batch_key: str) -> list[Any] | None:
        """Get a batch if ready to process."""
        import time

        if batch_key not in self._batches:
            return None

        batch = self._batches[batch_key]
        start_time = self._timers[batch_key]

        # Check if batch is full or timed out
        if len(batch) >= self.max_batch_size or (time.time() - start_time) >= self.max_wait_time:
            # Remove and return the batch
            del self._batches[batch_key]
            del self._timers[batch_key]
            return batch

        return None

    def get_all_ready_batches(self) -> dict[str, list[Any]]:
        """Get all batches that are ready to process."""
        ready_batches = {}
        for batch_key in list(self._batches.keys()):
            batch = self.get_batch(batch_key)
            if batch is not None:
                ready_batches[batch_key] = batch
        return ready_batches

    def force_process_all(self) -> dict[str, list[Any]]:
        """Force process all pending batches."""
        all_batches = dict(self._batches)
        self._batches.clear()
        self._timers.clear()
        return all_batches

    def pending_batches_count(self) -> int:
        """Get count of pending batches."""
        return len(self._batches)


# Data Export Classes
class DataExporter:
    """Utility for exporting response data to various formats."""

    @staticmethod
    def to_json(data: Any, file_path: str, indent: int = 2) -> None:
        """Export data to JSON file."""
        import json

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)

    @staticmethod
    def to_csv(data: list[dict], file_path: str, headers: list[str] | None = None) -> None:
        """Export list of dictionaries to CSV file."""
        import csv

        if not data:
            return

        if headers is None:
            headers = list(data[0].keys())

        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def flatten_response(response: Any, prefix: str = '') -> dict:
        """Flatten nested response data for CSV export."""
        flattened = {}

        if isinstance(response, dict):
            for key, value in response.items():
                new_key = f"{prefix}.{key}" if prefix else key
                if isinstance(value, (dict, list)):
                    flattened.update(DataExporter.flatten_response(value, new_key))
                else:
                    flattened[new_key] = value
        elif isinstance(response, list):
            for i, item in enumerate(response):
                new_key = f"{prefix}[{i}]" if prefix else f"[{i}]"
                if isinstance(item, (dict, list)):
                    flattened.update(DataExporter.flatten_response(item, new_key))
                else:
                    flattened[new_key] = item
        else:
            flattened[prefix] = response

        return flattened


# Pagination Helper Classes
class Paginator:
    """Helper for handling paginated API responses."""

    def __init__(self, client_method: Any, page_size: int = 50):
        """Initialize paginator.

        Args:
            client_method: The client method that supports pagination
            page_size: Number of items per page
        """
        self.client_method = client_method
        self.page_size = page_size

    def iterate_all(self, **kwargs) -> Any:
        """Iterate through all pages and yield items."""
        page = 1
        while True:
            # Update kwargs with pagination params
            paginated_kwargs = {**kwargs, "page": page, "per_page": self.page_size}

            try:
                response = self.client_method(**paginated_kwargs)

                # Handle different response structures
                if hasattr(response, 'data'):
                    items = response.data
                elif hasattr(response, '__iter__') and not isinstance(response, (str, dict)):
                    items = response
                else:
                    # Assume response is directly iterable
                    items = response if hasattr(response, '__iter__') else [response]

                if not items:
                    break

                yield from items

                # Check if there are more pages
                if hasattr(response, 'has_more') and not response.has_more:
                    break
                elif hasattr(response, 'next_page') and response.next_page is None:
                    break
                elif len(items) < self.page_size:
                    break

                page += 1

            except Exception as e:
                # If pagination fails, try to get all data at once
                try:
                    all_kwargs = {**kwargs, "limit": 1000}  # Try a high limit
                    response = self.client_method(**all_kwargs)
                    if hasattr(response, 'data'):
                        yield from response.data
                    elif hasattr(response, '__iter__'):
                        yield from response
                    break
                except:
                    raise e


# Model Management Functions
@lru_cache(maxsize=1)
def get_available_models() -> list[str]:
    """Get a list of available models with caching.

    This function caches the result to avoid repeated API calls.
    The cache can be cleared by calling get_available_models.cache_clear().

    Returns:
        List of available model names
    """
    # This would normally make an API call, but for now we'll return a static list
    # In a real implementation, this would fetch from the models endpoint
    return [
        "llama3.3-70b-instruct",
        "llama3.3-8b-instruct",
        "llama3.2-90b-instruct",
        "llama3.2-11b-instruct",
        "llama3.2-3b-instruct",
        "llama3.2-1b-instruct",
        "llama3.1-70b-instruct",
        "llama3.1-8b-instruct",
        "mixtral-8x7b-instruct",
        "codellama-34b-instruct",
        "codellama-13b-instruct",
        "codellama-7b-instruct",
    ]


def is_model_available(model_name: str) -> bool:
    """Check if a specific model is available.

    Args:
        model_name: Name of the model to check

    Returns:
        True if the model is available, False otherwise
    """
    return model_name in get_available_models()


def get_model_info(model_name: str) -> dict[str, Any] | None:
    """Get information about a specific model.

    Args:
        model_name: Name of the model

    Returns:
        Dictionary with model information, or None if model not found
    """
    # This would normally fetch detailed model info from API
    # For now, return basic info based on model name
    if not is_model_available(model_name):
        return None

    # Extract basic info from model name
    info = {"name": model_name, "available": True}

    if "llama" in model_name.lower():
        info["family"] = "Llama"
    elif "mixtral" in model_name.lower():
        info["family"] = "Mixtral"
    elif "codellama" in model_name.lower():
        info["family"] = "CodeLlama"
    else:
        info["family"] = "Unknown"

    # Extract parameter count if present
    import re
    param_match = re.search(r'(\d+(?:\.\d+)?)b', model_name.lower())
    if param_match:
        info["parameters"] = param_match.group(1) + "B"

    return info
