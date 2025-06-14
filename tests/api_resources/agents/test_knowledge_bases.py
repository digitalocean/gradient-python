# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types.agents import APILinkKnowledgeBaseOutput

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


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

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
