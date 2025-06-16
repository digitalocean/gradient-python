# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from . import api_keys_ as api_keys
from ...types import api_key_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.api_key_list_response import APIKeyListResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def api_keys(self) -> api_keys.APIKeysResource:
        return api_keys.APIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        public_only: bool | NotGiven = NOT_GIVEN,
        usecases: List[
            Literal[
                "MODEL_USECASE_UNKNOWN",
                "MODEL_USECASE_AGENT",
                "MODEL_USECASE_FINETUNED",
                "MODEL_USECASE_KNOWLEDGEBASE",
                "MODEL_USECASE_GUARDRAIL",
                "MODEL_USECASE_REASONING",
                "MODEL_USECASE_SERVERLESS",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIKeyListResponse:
        """
        To list all models, send a GET request to `/v2/gen-ai/models`.

        Args:
          page: page number.

          per_page: items per page.

          public_only: only include models that are publicly available.

          usecases: include only models defined for the listed usecases.

              - MODEL_USECASE_UNKNOWN: The use case of the model is unknown
              - MODEL_USECASE_AGENT: The model maybe used in an agent
              - MODEL_USECASE_FINETUNED: The model maybe used for fine tuning
              - MODEL_USECASE_KNOWLEDGEBASE: The model maybe used for knowledge bases
                (embedding models)
              - MODEL_USECASE_GUARDRAIL: The model maybe used for guardrails
              - MODEL_USECASE_REASONING: The model usecase for reasoning
              - MODEL_USECASE_SERVERLESS: The model usecase for serverless inference

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/gen-ai/models",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "public_only": public_only,
                        "usecases": usecases,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            cast_to=APIKeyListResponse,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResource:
        return api_keys.AsyncAPIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        public_only: bool | NotGiven = NOT_GIVEN,
        usecases: List[
            Literal[
                "MODEL_USECASE_UNKNOWN",
                "MODEL_USECASE_AGENT",
                "MODEL_USECASE_FINETUNED",
                "MODEL_USECASE_KNOWLEDGEBASE",
                "MODEL_USECASE_GUARDRAIL",
                "MODEL_USECASE_REASONING",
                "MODEL_USECASE_SERVERLESS",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIKeyListResponse:
        """
        To list all models, send a GET request to `/v2/gen-ai/models`.

        Args:
          page: page number.

          per_page: items per page.

          public_only: only include models that are publicly available.

          usecases: include only models defined for the listed usecases.

              - MODEL_USECASE_UNKNOWN: The use case of the model is unknown
              - MODEL_USECASE_AGENT: The model maybe used in an agent
              - MODEL_USECASE_FINETUNED: The model maybe used for fine tuning
              - MODEL_USECASE_KNOWLEDGEBASE: The model maybe used for knowledge bases
                (embedding models)
              - MODEL_USECASE_GUARDRAIL: The model maybe used for guardrails
              - MODEL_USECASE_REASONING: The model usecase for reasoning
              - MODEL_USECASE_SERVERLESS: The model usecase for serverless inference

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/gen-ai/models",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "public_only": public_only,
                        "usecases": usecases,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            cast_to=APIKeyListResponse,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = to_raw_response_wrapper(
            api_keys.list,
        )

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        return api_keys.APIKeysResourceWithRawResponse(self._api_keys.api_keys)


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        return api_keys.AsyncAPIKeysResourceWithRawResponse(self._api_keys.api_keys)


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        return api_keys.APIKeysResourceWithStreamingResponse(self._api_keys.api_keys)


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        return api_keys.AsyncAPIKeysResourceWithStreamingResponse(self._api_keys.api_keys)
