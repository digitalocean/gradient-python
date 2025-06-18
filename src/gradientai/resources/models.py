# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import model_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.model import Model
from .._base_client import make_request_options
from ..types.model_list_response import ModelListResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        model: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Model:
        """
        Retrieves a model instance, providing basic information about the model such as
        the owner and permissioning.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not model:
            raise ValueError(f"Expected a non-empty value for `model` but received {model!r}")
        return self._get(
            f"/models/{model}"
            if self._client._base_url_overridden
            else f"https://inference.do-ai.run/v1/models/{model}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Model,
        )

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
    ) -> ModelListResponse:
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
            "/v2/gen-ai/models"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/models",
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
                    model_list_params.ModelListParams,
                ),
            ),
            cast_to=ModelListResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/digitalocean/genai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/digitalocean/genai-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        model: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Model:
        """
        Retrieves a model instance, providing basic information about the model such as
        the owner and permissioning.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not model:
            raise ValueError(f"Expected a non-empty value for `model` but received {model!r}")
        return await self._get(
            f"/models/{model}"
            if self._client._base_url_overridden
            else f"https://inference.do-ai.run/v1/models/{model}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Model,
        )

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
    ) -> ModelListResponse:
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
            "/v2/gen-ai/models"
            if self._client._base_url_overridden
            else "https://api.digitalocean.com/v2/gen-ai/models",
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
                    model_list_params.ModelListParams,
                ),
            ),
            cast_to=ModelListResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.retrieve = to_raw_response_wrapper(
            models.retrieve,
        )
        self.list = to_raw_response_wrapper(
            models.list,
        )


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.retrieve = async_to_raw_response_wrapper(
            models.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            models.list,
        )


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.retrieve = to_streamed_response_wrapper(
            models.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            models.list,
        )


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.retrieve = async_to_streamed_response_wrapper(
            models.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            models.list,
        )
