from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `serverless_inference_sdk_prod.resources` module.

    This is used so that we can lazily import `serverless_inference_sdk_prod.resources` only when
    needed *and* so that users can just import `serverless_inference_sdk_prod` and reference `serverless_inference_sdk_prod.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("serverless_inference_sdk_prod.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
