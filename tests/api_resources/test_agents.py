# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import (
    AgentListResponse,
    AgentCreateResponse,
    AgentDeleteResponse,
    AgentUpdateResponse,
    AgentRetrieveResponse,
    AgentUpdateStatusResponse,
    AgentRetrieveUsageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        agent = client.agents.create()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        agent = client.agents.create(
            anthropic_key_uuid='"12345678-1234-1234-1234-123456789012"',
            description='"My Agent Description"',
            instruction='"You are an agent who thinks deeply about the world"',
            knowledge_base_uuid=["example string"],
            model_provider_key_uuid='"12345678-1234-1234-1234-123456789012"',
            model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My Agent"',
            openai_key_uuid='"12345678-1234-1234-1234-123456789012"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            region='"tor1"',
            tags=["example string"],
            workspace_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        agent = client.agents.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        agent = client.agents.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        agent = client.agents.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_log_insights_enabled=True,
            allowed_domains=["example string"],
            anthropic_key_uuid='"12345678-1234-1234-1234-123456789012"',
            conversation_logs_enabled=True,
            description='"My Agent Description"',
            instruction='"You are an agent who thinks deeply about the world"',
            k=5,
            max_tokens=100,
            model_provider_key_uuid='"12345678-1234-1234-1234-123456789012"',
            model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My New Agent Name"',
            openai_key_uuid='"12345678-1234-1234-1234-123456789012"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            provide_citations=True,
            retrieval_method="RETRIEVAL_METHOD_UNKNOWN",
            tags=["example string"],
            temperature=0.7,
            top_p=0.9,
            body_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.agents.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        agent = client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        agent = client.agents.list(
            only_deployed=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        agent = client.agents.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentDeleteResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_usage(self, client: Gradient) -> None:
        agent = client.agents.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_usage_with_all_params(self, client: Gradient) -> None:
        agent = client.agents.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
            start="start",
            stop="stop",
        )
        assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_usage(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_usage(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_usage(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.agents.with_raw_response.retrieve_usage(
                uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Gradient) -> None:
        agent = client.agents.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: Gradient) -> None:
        agent = client.agents.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_uuid='"12345678-1234-1234-1234-123456789012"',
            visibility="VISIBILITY_UNKNOWN",
        )
        assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Gradient) -> None:
        response = client.agents.with_raw_response.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Gradient) -> None:
        with client.agents.with_streaming_response.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            client.agents.with_raw_response.update_status(
                path_uuid="",
            )

    @parametrize
    def test_method_wait_until_ready(self, client: Gradient, respx_mock: Any) -> None:
        """Test successful wait_until_ready when agent becomes ready."""
        agent_uuid = "test-agent-id"

        # Create side effect that returns different responses
        call_count = [0]

        def get_response(_: httpx.Request) -> httpx.Response:
            call_count[0] += 1
            if call_count[0] == 1:
                # First call: deploying
                return httpx.Response(
                    200,
                    json={
                        "agent": {
                            "uuid": agent_uuid,
                            "deployment": {"status": "STATUS_DEPLOYING"},
                        }
                    },
                )
            else:
                # Subsequent calls: running
                return httpx.Response(
                    200,
                    json={
                        "agent": {
                            "uuid": agent_uuid,
                            "deployment": {"status": "STATUS_RUNNING"},
                        }
                    },
                )

        respx_mock.get(f"/v2/gen-ai/agents/{agent_uuid}").mock(side_effect=get_response)

        agent = client.agents.wait_until_ready(agent_uuid, poll_interval=0.1, timeout=10.0)
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])
        assert agent.agent is not None
        assert agent.agent.deployment is not None
        assert agent.agent.deployment.status == "STATUS_RUNNING"

    @parametrize
    def test_wait_until_ready_timeout(self, client: Gradient, respx_mock: Any) -> None:
        """Test that wait_until_ready raises timeout error."""
        from gradient._exceptions import AgentDeploymentTimeoutError

        agent_uuid = "test-agent-id"

        # Mock always returns deploying
        respx_mock.get(f"/v2/gen-ai/agents/{agent_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "agent": {
                        "uuid": agent_uuid,
                        "deployment": {"status": "STATUS_DEPLOYING"},
                    }
                },
            )
        )

        with pytest.raises(AgentDeploymentTimeoutError) as exc_info:
            client.agents.wait_until_ready(agent_uuid, poll_interval=0.1, timeout=0.5)

        assert "did not reach STATUS_RUNNING within" in str(exc_info.value)
        assert exc_info.value.agent_id == agent_uuid

    @parametrize
    def test_wait_until_ready_deployment_failed(self, client: Gradient, respx_mock: Any) -> None:
        """Test that wait_until_ready raises error on deployment failure."""
        from gradient._exceptions import AgentDeploymentError

        agent_uuid = "test-agent-id"

        # Mock returns failed status
        respx_mock.get(f"/v2/gen-ai/agents/{agent_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "agent": {
                        "uuid": agent_uuid,
                        "deployment": {"status": "STATUS_FAILED"},
                    }
                },
            )
        )

        with pytest.raises(AgentDeploymentError) as exc_info:
            client.agents.wait_until_ready(agent_uuid, poll_interval=0.1, timeout=10.0)

        assert "deployment failed with status: STATUS_FAILED" in str(exc_info.value)
        assert exc_info.value.status == "STATUS_FAILED"

    @parametrize
    def test_wait_until_ready_empty_uuid(self, client: Gradient) -> None:
        """Test that wait_until_ready validates empty uuid."""
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid`"):
            client.agents.wait_until_ready("")


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.create()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.create(
            anthropic_key_uuid='"12345678-1234-1234-1234-123456789012"',
            description='"My Agent Description"',
            instruction='"You are an agent who thinks deeply about the world"',
            knowledge_base_uuid=["example string"],
            model_provider_key_uuid='"12345678-1234-1234-1234-123456789012"',
            model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My Agent"',
            openai_key_uuid='"12345678-1234-1234-1234-123456789012"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            region='"tor1"',
            tags=["example string"],
            workspace_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            agent_log_insights_enabled=True,
            allowed_domains=["example string"],
            anthropic_key_uuid='"12345678-1234-1234-1234-123456789012"',
            conversation_logs_enabled=True,
            description='"My Agent Description"',
            instruction='"You are an agent who thinks deeply about the world"',
            k=5,
            max_tokens=100,
            model_provider_key_uuid='"12345678-1234-1234-1234-123456789012"',
            model_uuid='"12345678-1234-1234-1234-123456789012"',
            name='"My New Agent Name"',
            openai_key_uuid='"12345678-1234-1234-1234-123456789012"',
            project_id='"12345678-1234-1234-1234-123456789012"',
            provide_citations=True,
            retrieval_method="RETRIEVAL_METHOD_UNKNOWN",
            tags=["example string"],
            temperature=0.7,
            top_p=0.9,
            body_uuid='"12345678-1234-1234-1234-123456789012"',
        )
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.update(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.agents.with_raw_response.update(
                path_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.list(
            only_deployed=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentDeleteResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_usage(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_usage_with_all_params(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
            start="start",
            stop="stop",
        )
        assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_usage(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_usage(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.retrieve_usage(
            uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveUsageResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_usage(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.agents.with_raw_response.retrieve_usage(
                uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncGradient) -> None:
        agent = await async_client.agents.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            body_uuid='"12345678-1234-1234-1234-123456789012"',
            visibility="VISIBILITY_UNKNOWN",
        )
        assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.with_raw_response.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.with_streaming_response.update_status(
            path_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdateStatusResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_uuid` but received ''"):
            await async_client.agents.with_raw_response.update_status(
                path_uuid="",
            )

    @parametrize
    async def test_method_wait_until_ready(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Test successful async wait_until_ready when agent becomes ready."""
        agent_uuid = "test-agent-id"

        # Create side effect that returns different responses
        call_count = [0]

        def get_response(_: httpx.Request) -> httpx.Response:
            call_count[0] += 1
            if call_count[0] == 1:
                # First call: deploying
                return httpx.Response(
                    200,
                    json={
                        "agent": {
                            "uuid": agent_uuid,
                            "deployment": {"status": "STATUS_DEPLOYING"},
                        }
                    },
                )
            else:
                # Subsequent calls: running
                return httpx.Response(
                    200,
                    json={
                        "agent": {
                            "uuid": agent_uuid,
                            "deployment": {"status": "STATUS_RUNNING"},
                        }
                    },
                )

        respx_mock.get(f"/v2/gen-ai/agents/{agent_uuid}").mock(side_effect=get_response)

        agent = await async_client.agents.wait_until_ready(agent_uuid, poll_interval=0.1, timeout=10.0)
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])
        assert agent.agent is not None
        assert agent.agent.deployment is not None
        assert agent.agent.deployment.status == "STATUS_RUNNING"

    @parametrize
    async def test_wait_until_ready_timeout(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Test that async wait_until_ready raises timeout error."""
        from gradient._exceptions import AgentDeploymentTimeoutError

        agent_uuid = "test-agent-id"

        # Mock always returns deploying
        respx_mock.get(f"/v2/gen-ai/agents/{agent_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "agent": {
                        "uuid": agent_uuid,
                        "deployment": {"status": "STATUS_DEPLOYING"},
                    }
                },
            )
        )

        with pytest.raises(AgentDeploymentTimeoutError) as exc_info:
            await async_client.agents.wait_until_ready(agent_uuid, poll_interval=0.1, timeout=0.5)

        assert "did not reach STATUS_RUNNING within" in str(exc_info.value)
        assert exc_info.value.agent_id == agent_uuid

    @parametrize
    async def test_wait_until_ready_deployment_failed(self, async_client: AsyncGradient, respx_mock: Any) -> None:
        """Test that async wait_until_ready raises error on deployment failure."""
        from gradient._exceptions import AgentDeploymentError

        agent_uuid = "test-agent-id"

        # Mock returns failed status
        respx_mock.get(f"/v2/gen-ai/agents/{agent_uuid}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "agent": {
                        "uuid": agent_uuid,
                        "deployment": {"status": "STATUS_FAILED"},
                    }
                },
            )
        )

        with pytest.raises(AgentDeploymentError) as exc_info:
            await async_client.agents.wait_until_ready(agent_uuid, poll_interval=0.1, timeout=10.0)

        assert "deployment failed with status: STATUS_FAILED" in str(exc_info.value)
        assert exc_info.value.status == "STATUS_FAILED"
