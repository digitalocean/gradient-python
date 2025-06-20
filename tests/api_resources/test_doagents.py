# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types import (
    DoagentListResponse,
    DoagentCreateResponse,
    DoagentDeleteResponse,
    DoagentUpdateResponse,
    DoagentRetrieveResponse,
    DoagentUpdateStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDoagents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GradientAI) -> None:
        doagent = client.doagents.create()
        assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GradientAI) -> None:
        doagent = client.doagents.create(
            anthropic_key_uuid="anthropic_key_uuid",
            description="description",
            instruction="instruction",
            knowledge_base_uuid=["string"],
            model_uuid="model_uuid",
            name="name",
            openai_key_uuid="open_ai_key_uuid",
            project_id="project_id",
            region="region",
            tags=["string"],
        )
        assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GradientAI) -> None:
        response = client.doagents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = response.parse()
        assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GradientAI) -> None:
        with client.doagents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = response.parse()
            assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: GradientAI) -> None:
        doagent = client.doagents.retrieve(
            "uuid",
        )
        assert_matches_type(DoagentRetrieveResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: GradientAI) -> None:
        response = client.doagents.with_raw_response.retrieve(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = response.parse()
        assert_matches_type(DoagentRetrieveResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: GradientAI) -> None:
        with client.doagents.with_streaming_response.retrieve(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = response.parse()
            assert_matches_type(DoagentRetrieveResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.doagents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: GradientAI) -> None:
        doagent = client.doagents.update(
            path_uuid="uuid",
        )
        assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: GradientAI) -> None:
        doagent = client.doagents.update(
            path_uuid="uuid",
            anthropic_key_uuid="anthropic_key_uuid",
            description="description",
            instruction="instruction",
            k=0,
            max_tokens=0,
            model_uuid="model_uuid",
            name="name",
            openai_key_uuid="open_ai_key_uuid",
            project_id="project_id",
            provide_citations=True,
            retrieval_method="RETRIEVAL_METHOD_UNKNOWN",
            tags=["string"],
            temperature=0,
            top_p=0,
            body_uuid="uuid",
        )
        assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: GradientAI) -> None:
        response = client.doagents.with_raw_response.update(
            path_uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = response.parse()
        assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: GradientAI) -> None:
        with client.doagents.with_streaming_response.update(
            path_uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = response.parse()
            assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.doagents.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        doagent = client.doagents.list()
        assert_matches_type(DoagentListResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        doagent = client.doagents.list(
            only_deployed=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(DoagentListResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.doagents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = response.parse()
        assert_matches_type(DoagentListResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.doagents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = response.parse()
            assert_matches_type(DoagentListResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: GradientAI) -> None:
        doagent = client.doagents.delete(
            "uuid",
        )
        assert_matches_type(DoagentDeleteResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: GradientAI) -> None:
        response = client.doagents.with_raw_response.delete(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = response.parse()
        assert_matches_type(DoagentDeleteResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: GradientAI) -> None:
        with client.doagents.with_streaming_response.delete(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = response.parse()
            assert_matches_type(DoagentDeleteResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.doagents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_status(self, client: GradientAI) -> None:
        doagent = client.doagents.update_status(
            path_uuid="uuid",
        )
        assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_status_with_all_params(self, client: GradientAI) -> None:
        doagent = client.doagents.update_status(
            path_uuid="uuid",
            body_uuid="uuid",
            visibility="VISIBILITY_UNKNOWN",
        )
        assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_status(self, client: GradientAI) -> None:
        response = client.doagents.with_raw_response.update_status(
            path_uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = response.parse()
        assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_status(self, client: GradientAI) -> None:
        with client.doagents.with_streaming_response.update_status(
            path_uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = response.parse()
            assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_status(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.doagents.with_raw_response.update_status(
                path_uuid="",
            )


class TestAsyncDoagents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.create()
        assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.create(
            anthropic_key_uuid="anthropic_key_uuid",
            description="description",
            instruction="instruction",
            knowledge_base_uuid=["string"],
            model_uuid="model_uuid",
            name="name",
            openai_key_uuid="open_ai_key_uuid",
            project_id="project_id",
            region="region",
            tags=["string"],
        )
        assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.doagents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = await response.parse()
        assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradientAI) -> None:
        async with async_client.doagents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = await response.parse()
            assert_matches_type(DoagentCreateResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.retrieve(
            "uuid",
        )
        assert_matches_type(DoagentRetrieveResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.doagents.with_raw_response.retrieve(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = await response.parse()
        assert_matches_type(DoagentRetrieveResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradientAI) -> None:
        async with async_client.doagents.with_streaming_response.retrieve(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = await response.parse()
            assert_matches_type(DoagentRetrieveResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.doagents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.update(
            path_uuid="uuid",
        )
        assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.update(
            path_uuid="uuid",
            anthropic_key_uuid="anthropic_key_uuid",
            description="description",
            instruction="instruction",
            k=0,
            max_tokens=0,
            model_uuid="model_uuid",
            name="name",
            openai_key_uuid="open_ai_key_uuid",
            project_id="project_id",
            provide_citations=True,
            retrieval_method="RETRIEVAL_METHOD_UNKNOWN",
            tags=["string"],
            temperature=0,
            top_p=0,
            body_uuid="uuid",
        )
        assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.doagents.with_raw_response.update(
            path_uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = await response.parse()
        assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradientAI) -> None:
        async with async_client.doagents.with_streaming_response.update(
            path_uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = await response.parse()
            assert_matches_type(DoagentUpdateResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.doagents.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.list()
        assert_matches_type(DoagentListResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.list(
            only_deployed=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(DoagentListResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.doagents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = await response.parse()
        assert_matches_type(DoagentListResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.doagents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = await response.parse()
            assert_matches_type(DoagentListResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.delete(
            "uuid",
        )
        assert_matches_type(DoagentDeleteResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.doagents.with_raw_response.delete(
            "uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = await response.parse()
        assert_matches_type(DoagentDeleteResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradientAI) -> None:
        async with async_client.doagents.with_streaming_response.delete(
            "uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = await response.parse()
            assert_matches_type(DoagentDeleteResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.doagents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_status(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.update_status(
            path_uuid="uuid",
        )
        assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncGradientAI) -> None:
        doagent = await async_client.doagents.update_status(
            path_uuid="uuid",
            body_uuid="uuid",
            visibility="VISIBILITY_UNKNOWN",
        )
        assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.doagents.with_raw_response.update_status(
            path_uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doagent = await response.parse()
        assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncGradientAI) -> None:
        async with async_client.doagents.with_streaming_response.update_status(
            path_uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doagent = await response.parse()
            assert_matches_type(DoagentUpdateStatusResponse, doagent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.doagents.with_raw_response.update_status(
                path_uuid="",
            )
