# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradientai import GradientAI, AsyncGradientAI
from tests.utils import assert_matches_type
from gradientai.types.agents.evaluation_metrics.workspaces import (
    AgentListResponse,
    AgentMoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: GradientAI) -> None:
        agent = client.agents.evaluation_metrics.workspaces.agents.list(
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: GradientAI) -> None:
        agent = client.agents.evaluation_metrics.workspaces.agents.list(
            workspace_uuid="workspace_uuid",
            field_mask={"paths": ["string"]},
            only_deployed=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: GradientAI) -> None:
        response = client.agents.evaluation_metrics.workspaces.agents.with_raw_response.list(
            workspace_uuid="workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: GradientAI) -> None:
        with client.agents.evaluation_metrics.workspaces.agents.with_streaming_response.list(
            workspace_uuid="workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.agents.evaluation_metrics.workspaces.agents.with_raw_response.list(
                workspace_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_move(self, client: GradientAI) -> None:
        agent = client.agents.evaluation_metrics.workspaces.agents.move(
            path_workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AgentMoveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_move_with_all_params(self, client: GradientAI) -> None:
        agent = client.agents.evaluation_metrics.workspaces.agents.move(
            path_workspace_uuid="workspace_uuid",
            agent_uuids=["string"],
            body_workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AgentMoveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_move(self, client: GradientAI) -> None:
        response = client.agents.evaluation_metrics.workspaces.agents.with_raw_response.move(
            path_workspace_uuid="workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentMoveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_move(self, client: GradientAI) -> None:
        with client.agents.evaluation_metrics.workspaces.agents.with_streaming_response.move(
            path_workspace_uuid="workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentMoveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_move(self, client: GradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_workspace_uuid` but received ''"):
            client.agents.evaluation_metrics.workspaces.agents.with_raw_response.move(
                path_workspace_uuid="",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGradientAI) -> None:
        agent = await async_client.agents.evaluation_metrics.workspaces.agents.list(
            workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradientAI) -> None:
        agent = await async_client.agents.evaluation_metrics.workspaces.agents.list(
            workspace_uuid="workspace_uuid",
            field_mask={"paths": ["string"]},
            only_deployed=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.agents.with_raw_response.list(
            workspace_uuid="workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradientAI) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.agents.with_streaming_response.list(
            workspace_uuid="workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.workspaces.agents.with_raw_response.list(
                workspace_uuid="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_move(self, async_client: AsyncGradientAI) -> None:
        agent = await async_client.agents.evaluation_metrics.workspaces.agents.move(
            path_workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AgentMoveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncGradientAI) -> None:
        agent = await async_client.agents.evaluation_metrics.workspaces.agents.move(
            path_workspace_uuid="workspace_uuid",
            agent_uuids=["string"],
            body_workspace_uuid="workspace_uuid",
        )
        assert_matches_type(AgentMoveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncGradientAI) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.agents.with_raw_response.move(
            path_workspace_uuid="workspace_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentMoveResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncGradientAI) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.agents.with_streaming_response.move(
            path_workspace_uuid="workspace_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentMoveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_move(self, async_client: AsyncGradientAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_workspace_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.workspaces.agents.with_raw_response.move(
                path_workspace_uuid="",
            )
