# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.apps import JobInvocationCancelResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobInvocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Gradient) -> None:
        job_invocation = client.apps.job_invocations.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
        )
        assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Gradient) -> None:
        job_invocation = client.apps.job_invocations.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
            job_name="job_name",
        )
        assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Gradient) -> None:
        response = client.apps.job_invocations.with_raw_response.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_invocation = response.parse()
        assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Gradient) -> None:
        with client.apps.job_invocations.with_streaming_response.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_invocation = response.parse()
            assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.job_invocations.with_raw_response.cancel(
                job_invocation_id="123e4567-e89b-12d3-a456-426",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_invocation_id` but received ''"):
            client.apps.job_invocations.with_raw_response.cancel(
                job_invocation_id="",
                app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
            )


class TestAsyncJobInvocations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncGradient) -> None:
        job_invocation = await async_client.apps.job_invocations.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
        )
        assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncGradient) -> None:
        job_invocation = await async_client.apps.job_invocations.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
            job_name="job_name",
        )
        assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncGradient) -> None:
        response = await async_client.apps.job_invocations.with_raw_response.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_invocation = await response.parse()
        assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncGradient) -> None:
        async with async_client.apps.job_invocations.with_streaming_response.cancel(
            job_invocation_id="123e4567-e89b-12d3-a456-426",
            app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_invocation = await response.parse()
            assert_matches_type(JobInvocationCancelResponse, job_invocation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.job_invocations.with_raw_response.cancel(
                job_invocation_id="123e4567-e89b-12d3-a456-426",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_invocation_id` but received ''"):
            await async_client.apps.job_invocations.with_raw_response.cancel(
                job_invocation_id="",
                app_id="4f6c71e2-1e90-4762-9fee-6cc4a0a9f2cf",
            )
