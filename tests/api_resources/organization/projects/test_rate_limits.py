# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types.organization.projects import (
    ProjectRateLimit,
    RateLimitListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRateLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: ServerlessInferenceSDKProd) -> None:
        rate_limit = client.organization.projects.rate_limits.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
        )
        assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        rate_limit = client.organization.projects.rate_limits.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
            batch_1_day_max_input_tokens=0,
            max_audio_megabytes_per_1_minute=0,
            max_images_per_1_minute=0,
            max_requests_per_1_day=0,
            max_requests_per_1_minute=0,
            max_tokens_per_1_minute=0,
        )
        assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.rate_limits.with_raw_response.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.rate_limits.with_streaming_response.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = response.parse()
            assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.rate_limits.with_raw_response.update(
                rate_limit_id="rate_limit_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
            client.organization.projects.rate_limits.with_raw_response.update(
                rate_limit_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: ServerlessInferenceSDKProd) -> None:
        rate_limit = client.organization.projects.rate_limits.list(
            project_id="project_id",
        )
        assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        rate_limit = client.organization.projects.rate_limits.list(
            project_id="project_id",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.rate_limits.with_raw_response.list(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.rate_limits.with_streaming_response.list(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = response.parse()
            assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.rate_limits.with_raw_response.list(
                project_id="",
            )


class TestAsyncRateLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        rate_limit = await async_client.organization.projects.rate_limits.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
        )
        assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        rate_limit = await async_client.organization.projects.rate_limits.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
            batch_1_day_max_input_tokens=0,
            max_audio_megabytes_per_1_minute=0,
            max_images_per_1_minute=0,
            max_requests_per_1_day=0,
            max_requests_per_1_minute=0,
            max_tokens_per_1_minute=0,
        )
        assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.rate_limits.with_raw_response.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.rate_limits.with_streaming_response.update(
            rate_limit_id="rate_limit_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = await response.parse()
            assert_matches_type(ProjectRateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.rate_limits.with_raw_response.update(
                rate_limit_id="rate_limit_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
            await async_client.organization.projects.rate_limits.with_raw_response.update(
                rate_limit_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        rate_limit = await async_client.organization.projects.rate_limits.list(
            project_id="project_id",
        )
        assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        rate_limit = await async_client.organization.projects.rate_limits.list(
            project_id="project_id",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.rate_limits.with_raw_response.list(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.rate_limits.with_streaming_response.list(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = await response.parse()
            assert_matches_type(RateLimitListResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.rate_limits.with_raw_response.list(
                project_id="",
            )
