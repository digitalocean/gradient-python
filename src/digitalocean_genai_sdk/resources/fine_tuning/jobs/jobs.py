# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .checkpoints import (
    CheckpointsResource,
    AsyncCheckpointsResource,
    CheckpointsResourceWithRawResponse,
    AsyncCheckpointsResourceWithRawResponse,
    CheckpointsResourceWithStreamingResponse,
    AsyncCheckpointsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.fine_tuning import job_list_params, job_create_params
from ....types.fine_tuning.fine_tuning_job import FineTuningJob
from ....types.fine_tuning.job_list_response import JobListResponse
from ....types.fine_tuning.fine_tune_method_param import FineTuneMethodParam

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def checkpoints(self) -> CheckpointsResource:
        return CheckpointsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: Union[str, Literal["babbage-002", "davinci-002", "gpt-3.5-turbo", "gpt-4o-mini"]],
        training_file: str,
        hyperparameters: job_create_params.Hyperparameters | NotGiven = NOT_GIVEN,
        integrations: Optional[Iterable[job_create_params.Integration]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        method: FineTuneMethodParam | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        validation_file: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuningJob:
        """
        Creates a fine-tuning job which begins the process of creating a new model from
        a given dataset.

        Response includes details of the enqueued job including job status and the name
        of the fine-tuned models once complete.

        [Learn more about fine-tuning](/docs/guides/fine-tuning)

        Args:
          model: The name of the model to fine-tune. You can select one of the
              [supported models](/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

          training_file: The ID of an uploaded file that contains training data.

              See [upload file](/docs/api-reference/files/create) for how to upload a file.

              Your dataset must be formatted as a JSONL file. Additionally, you must upload
              your file with the purpose `fine-tune`.

              The contents of the file should differ depending on if the model uses the
              [chat](/docs/api-reference/fine-tuning/chat-input),
              [completions](/docs/api-reference/fine-tuning/completions-input) format, or if
              the fine-tuning method uses the
              [preference](/docs/api-reference/fine-tuning/preference-input) format.

              See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

          hyperparameters: The hyperparameters used for the fine-tuning job. This value is now deprecated
              in favor of `method`, and should be passed in under the `method` parameter.

          integrations: A list of integrations to enable for your fine-tuning job.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          method: The method used for fine-tuning.

          seed: The seed controls the reproducibility of the job. Passing in the same seed and
              job parameters should produce the same results, but may differ in rare cases. If
              a seed is not specified, one will be generated for you.

          suffix: A string of up to 64 characters that will be added to your fine-tuned model
              name.

              For example, a `suffix` of "custom-model-name" would produce a model name like
              `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

          validation_file: The ID of an uploaded file that contains validation data.

              If you provide this file, the data is used to generate validation metrics
              periodically during fine-tuning. These metrics can be viewed in the fine-tuning
              results file. The same data should not be present in both train and validation
              files.

              Your dataset must be formatted as a JSONL file. You must upload your file with
              the purpose `fine-tune`.

              See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fine_tuning/jobs",
            body=maybe_transform(
                {
                    "model": model,
                    "training_file": training_file,
                    "hyperparameters": hyperparameters,
                    "integrations": integrations,
                    "metadata": metadata,
                    "method": method,
                    "seed": seed,
                    "suffix": suffix,
                    "validation_file": validation_file,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuningJob,
        )

    def retrieve(
        self,
        fine_tuning_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuningJob:
        """
        Get info about a fine-tuning job.

        [Learn more about fine-tuning](/docs/guides/fine-tuning)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return self._get(
            f"/fine_tuning/jobs/{fine_tuning_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuningJob,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
        """
        List your organization's fine-tuning jobs

        Args:
          after: Identifier for the last job from the previous pagination request.

          limit: Number of fine-tuning jobs to retrieve.

          metadata: Optional metadata filter. To filter, use the syntax `metadata[k]=v`.
              Alternatively, set `metadata=null` to indicate no metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fine_tuning/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "metadata": metadata,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    def cancel(
        self,
        fine_tuning_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuningJob:
        """
        Immediately cancel a fine-tune job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return self._post(
            f"/fine_tuning/jobs/{fine_tuning_job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuningJob,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def checkpoints(self) -> AsyncCheckpointsResource:
        return AsyncCheckpointsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: Union[str, Literal["babbage-002", "davinci-002", "gpt-3.5-turbo", "gpt-4o-mini"]],
        training_file: str,
        hyperparameters: job_create_params.Hyperparameters | NotGiven = NOT_GIVEN,
        integrations: Optional[Iterable[job_create_params.Integration]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        method: FineTuneMethodParam | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        validation_file: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuningJob:
        """
        Creates a fine-tuning job which begins the process of creating a new model from
        a given dataset.

        Response includes details of the enqueued job including job status and the name
        of the fine-tuned models once complete.

        [Learn more about fine-tuning](/docs/guides/fine-tuning)

        Args:
          model: The name of the model to fine-tune. You can select one of the
              [supported models](/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

          training_file: The ID of an uploaded file that contains training data.

              See [upload file](/docs/api-reference/files/create) for how to upload a file.

              Your dataset must be formatted as a JSONL file. Additionally, you must upload
              your file with the purpose `fine-tune`.

              The contents of the file should differ depending on if the model uses the
              [chat](/docs/api-reference/fine-tuning/chat-input),
              [completions](/docs/api-reference/fine-tuning/completions-input) format, or if
              the fine-tuning method uses the
              [preference](/docs/api-reference/fine-tuning/preference-input) format.

              See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

          hyperparameters: The hyperparameters used for the fine-tuning job. This value is now deprecated
              in favor of `method`, and should be passed in under the `method` parameter.

          integrations: A list of integrations to enable for your fine-tuning job.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          method: The method used for fine-tuning.

          seed: The seed controls the reproducibility of the job. Passing in the same seed and
              job parameters should produce the same results, but may differ in rare cases. If
              a seed is not specified, one will be generated for you.

          suffix: A string of up to 64 characters that will be added to your fine-tuned model
              name.

              For example, a `suffix` of "custom-model-name" would produce a model name like
              `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

          validation_file: The ID of an uploaded file that contains validation data.

              If you provide this file, the data is used to generate validation metrics
              periodically during fine-tuning. These metrics can be viewed in the fine-tuning
              results file. The same data should not be present in both train and validation
              files.

              Your dataset must be formatted as a JSONL file. You must upload your file with
              the purpose `fine-tune`.

              See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fine_tuning/jobs",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "training_file": training_file,
                    "hyperparameters": hyperparameters,
                    "integrations": integrations,
                    "metadata": metadata,
                    "method": method,
                    "seed": seed,
                    "suffix": suffix,
                    "validation_file": validation_file,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuningJob,
        )

    async def retrieve(
        self,
        fine_tuning_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuningJob:
        """
        Get info about a fine-tuning job.

        [Learn more about fine-tuning](/docs/guides/fine-tuning)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return await self._get(
            f"/fine_tuning/jobs/{fine_tuning_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuningJob,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
        """
        List your organization's fine-tuning jobs

        Args:
          after: Identifier for the last job from the previous pagination request.

          limit: Number of fine-tuning jobs to retrieve.

          metadata: Optional metadata filter. To filter, use the syntax `metadata[k]=v`.
              Alternatively, set `metadata=null` to indicate no metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fine_tuning/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "metadata": metadata,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    async def cancel(
        self,
        fine_tuning_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuningJob:
        """
        Immediately cancel a fine-tune job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return await self._post(
            f"/fine_tuning/jobs/{fine_tuning_job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuningJob,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.cancel = to_raw_response_wrapper(
            jobs.cancel,
        )

    @cached_property
    def checkpoints(self) -> CheckpointsResourceWithRawResponse:
        return CheckpointsResourceWithRawResponse(self._jobs.checkpoints)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._jobs.events)


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            jobs.cancel,
        )

    @cached_property
    def checkpoints(self) -> AsyncCheckpointsResourceWithRawResponse:
        return AsyncCheckpointsResourceWithRawResponse(self._jobs.checkpoints)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._jobs.events)


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.cancel = to_streamed_response_wrapper(
            jobs.cancel,
        )

    @cached_property
    def checkpoints(self) -> CheckpointsResourceWithStreamingResponse:
        return CheckpointsResourceWithStreamingResponse(self._jobs.checkpoints)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._jobs.events)


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            jobs.cancel,
        )

    @cached_property
    def checkpoints(self) -> AsyncCheckpointsResourceWithStreamingResponse:
        return AsyncCheckpointsResourceWithStreamingResponse(self._jobs.checkpoints)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._jobs.events)
