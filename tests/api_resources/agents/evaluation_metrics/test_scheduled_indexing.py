# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents.evaluation_metrics import (
    ScheduledIndexingCreateResponse,
    ScheduledIndexingDeleteResponse,
    ScheduledIndexingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduledIndexing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        scheduled_indexing = client.agents.evaluation_metrics.scheduled_indexing.create()
        assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        scheduled_indexing = client.agents.evaluation_metrics.scheduled_indexing.create(
            days=[123],
            knowledge_base_uuid="123e4567-e89b-12d3-a456-426614174000",
            time="example string",
        )
        assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_indexing = response.parse()
        assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.scheduled_indexing.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_indexing = response.parse()
            assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        scheduled_indexing = client.agents.evaluation_metrics.scheduled_indexing.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(ScheduledIndexingRetrieveResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_indexing = response.parse()
        assert_matches_type(ScheduledIndexingRetrieveResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.scheduled_indexing.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_indexing = response.parse()
            assert_matches_type(ScheduledIndexingRetrieveResponse, scheduled_indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        scheduled_indexing = client.agents.evaluation_metrics.scheduled_indexing.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(ScheduledIndexingDeleteResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_indexing = response.parse()
        assert_matches_type(ScheduledIndexingDeleteResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.scheduled_indexing.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_indexing = response.parse()
            assert_matches_type(ScheduledIndexingDeleteResponse, scheduled_indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.delete(
                "",
            )


class TestAsyncScheduledIndexing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        scheduled_indexing = await async_client.agents.evaluation_metrics.scheduled_indexing.create()
        assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        scheduled_indexing = await async_client.agents.evaluation_metrics.scheduled_indexing.create(
            days=[123],
            knowledge_base_uuid="123e4567-e89b-12d3-a456-426614174000",
            time="example string",
        )
        assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_indexing = await response.parse()
        assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with (
            async_client.agents.evaluation_metrics.scheduled_indexing.with_streaming_response.create()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_indexing = await response.parse()
            assert_matches_type(ScheduledIndexingCreateResponse, scheduled_indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        scheduled_indexing = await async_client.agents.evaluation_metrics.scheduled_indexing.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(ScheduledIndexingRetrieveResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_indexing = await response.parse()
        assert_matches_type(ScheduledIndexingRetrieveResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.scheduled_indexing.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_indexing = await response.parse()
            assert_matches_type(ScheduledIndexingRetrieveResponse, scheduled_indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        scheduled_indexing = await async_client.agents.evaluation_metrics.scheduled_indexing.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(ScheduledIndexingDeleteResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled_indexing = await response.parse()
        assert_matches_type(ScheduledIndexingDeleteResponse, scheduled_indexing, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.scheduled_indexing.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled_indexing = await response.parse()
            assert_matches_type(ScheduledIndexingDeleteResponse, scheduled_indexing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.agents.evaluation_metrics.scheduled_indexing.with_raw_response.delete(
                "",
            )
