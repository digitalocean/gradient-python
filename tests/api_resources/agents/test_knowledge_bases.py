# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from do_gradientai import GradientAI, AsyncGradientAI
from do_gradientai.types.agents import APILinkKnowledgeBaseOutput, KnowledgeBaseDetachResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_attach(self, client: GradientAI) -> None:
        knowledge_base = client.agents.knowledge_bases.attach(
            "agent_uuid",
        )
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_attach(self, client: GradientAI) -> None:
        response = client.agents.knowledge_bases.with_raw_response.attach(
            "agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_attach(self, client: GradientAI) -> None:
        with client.agents.knowledge_bases.with_streaming_response.attach(
            "agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_attach(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.agents.knowledge_bases.with_raw_response.attach(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_attach_single(self, client: GradientAI) -> None:
        knowledge_base = client.agents.knowledge_bases.attach_single(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_attach_single(self, client: GradientAI) -> None:
        response = client.agents.knowledge_bases.with_raw_response.attach_single(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_attach_single(self, client: GradientAI) -> None:
        with client.agents.knowledge_bases.with_streaming_response.attach_single(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_attach_single(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.agents.knowledge_bases.with_raw_response.attach_single(
                knowledge_base_uuid="knowledge_base_uuid",
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.agents.knowledge_bases.with_raw_response.attach_single(
                knowledge_base_uuid="",
                agent_uuid="agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_detach(self, client: GradientAI) -> None:
        knowledge_base = client.agents.knowledge_bases.detach(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )
        assert_matches_type(KnowledgeBaseDetachResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_detach(self, client: GradientAI) -> None:
        response = client.agents.knowledge_bases.with_raw_response.detach(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseDetachResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_detach(self, client: GradientAI) -> None:
        with client.agents.knowledge_bases.with_streaming_response.detach(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseDetachResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_detach(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.agents.knowledge_bases.with_raw_response.detach(
                knowledge_base_uuid="knowledge_base_uuid",
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            client.agents.knowledge_bases.with_raw_response.detach(
                knowledge_base_uuid="",
                agent_uuid="agent_uuid",
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_attach(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.agents.knowledge_bases.attach(
            "agent_uuid",
        )
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.agents.knowledge_bases.with_raw_response.attach(
            "agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncGradientAI) -> None:
        async with async_client.agents.knowledge_bases.with_streaming_response.attach(
            "agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.agents.knowledge_bases.with_raw_response.attach(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_attach_single(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.agents.knowledge_bases.attach_single(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_attach_single(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.agents.knowledge_bases.with_raw_response.attach_single(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_attach_single(self, async_client: AsyncGradientAI) -> None:
        async with async_client.agents.knowledge_bases.with_streaming_response.attach_single(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APILinkKnowledgeBaseOutput, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_attach_single(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.agents.knowledge_bases.with_raw_response.attach_single(
                knowledge_base_uuid="knowledge_base_uuid",
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.agents.knowledge_bases.with_raw_response.attach_single(
                knowledge_base_uuid="",
                agent_uuid="agent_uuid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_detach(self, async_client: AsyncGradientAI) -> None:
        knowledge_base = await async_client.agents.knowledge_bases.detach(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )
        assert_matches_type(KnowledgeBaseDetachResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.agents.knowledge_bases.with_raw_response.detach(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseDetachResponse, knowledge_base, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncGradientAI) -> None:
        async with async_client.agents.knowledge_bases.with_streaming_response.detach(
            knowledge_base_uuid="knowledge_base_uuid",
            agent_uuid="agent_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseDetachResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.agents.knowledge_bases.with_raw_response.detach(
                knowledge_base_uuid="knowledge_base_uuid",
                agent_uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_uuid` but received ''"):
            await async_client.agents.knowledge_bases.with_raw_response.detach(
                knowledge_base_uuid="",
                agent_uuid="agent_uuid",
            )
