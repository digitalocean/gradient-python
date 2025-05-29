# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types import UsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_audio_speeches(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.audio_speeches(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_audio_speeches_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.audio_speeches(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_audio_speeches(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.audio_speeches(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_audio_speeches(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.audio_speeches(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_audio_transcriptions(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.audio_transcriptions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_audio_transcriptions_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.audio_transcriptions(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_audio_transcriptions(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.audio_transcriptions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_audio_transcriptions(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.audio_transcriptions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_code_interpreter_sessions(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.code_interpreter_sessions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_code_interpreter_sessions_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.code_interpreter_sessions(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_code_interpreter_sessions(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.code_interpreter_sessions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_code_interpreter_sessions(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.code_interpreter_sessions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_completions(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.completions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_completions_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.completions(
            start_time=0,
            api_key_ids=["string"],
            batch=True,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_completions(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.completions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_completions(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.completions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_embeddings(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.embeddings(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_embeddings_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.embeddings(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_embeddings(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.embeddings(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_embeddings(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.embeddings(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_images(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.images(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_images_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.images(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            sizes=["256x256"],
            sources=["image.generation"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_images(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.images(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_images(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.images(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_moderations(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.moderations(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_moderations_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.moderations(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_moderations(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.moderations(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_moderations(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.moderations(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_vector_stores(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.vector_stores(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_vector_stores_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        usage = client.organization.usage.vector_stores(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_vector_stores(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.organization.usage.with_raw_response.vector_stores(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_vector_stores(self, client: DigitaloceanGenaiSDK) -> None:
        with client.organization.usage.with_streaming_response.vector_stores(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_audio_speeches(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.audio_speeches(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_audio_speeches_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.audio_speeches(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_audio_speeches(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.audio_speeches(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_audio_speeches(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.audio_speeches(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_audio_transcriptions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.audio_transcriptions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_audio_transcriptions_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.audio_transcriptions(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_audio_transcriptions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.audio_transcriptions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_audio_transcriptions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.audio_transcriptions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_code_interpreter_sessions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.code_interpreter_sessions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_code_interpreter_sessions_with_all_params(
        self, async_client: AsyncDigitaloceanGenaiSDK
    ) -> None:
        usage = await async_client.organization.usage.code_interpreter_sessions(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_code_interpreter_sessions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.code_interpreter_sessions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_code_interpreter_sessions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.code_interpreter_sessions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_completions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.completions(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_completions_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.completions(
            start_time=0,
            api_key_ids=["string"],
            batch=True,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_completions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.completions(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_completions(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.completions(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_embeddings(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.embeddings(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_embeddings_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.embeddings(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_embeddings(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.embeddings(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_embeddings(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.embeddings(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_images(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.images(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_images_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.images(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            sizes=["256x256"],
            sources=["image.generation"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_images(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.images(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_images(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.images(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_moderations(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.moderations(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_moderations_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.moderations(
            start_time=0,
            api_key_ids=["string"],
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            models=["string"],
            page="page",
            project_ids=["string"],
            user_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_moderations(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.moderations(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_moderations(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.moderations(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_vector_stores(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.vector_stores(
            start_time=0,
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_vector_stores_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        usage = await async_client.organization.usage.vector_stores(
            start_time=0,
            bucket_width="1m",
            end_time=0,
            group_by=["project_id"],
            limit=0,
            page="page",
            project_ids=["string"],
        )
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_vector_stores(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.organization.usage.with_raw_response.vector_stores(
            start_time=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageResponse, usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_vector_stores(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.organization.usage.with_streaming_response.vector_stores(
            start_time=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
