# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.agents.evaluation_metrics import (
    WorkspaceListResponse,
    WorkspaceCreateResponse,
    WorkspaceDeleteResponse,
    WorkspaceUpdateResponse,
    WorkspaceRetrieveResponse,
    WorkspaceListEvaluationTestCasesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.create()
        assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.create(
            agent_uuids=["example string"],
            description="example string",
            name="example name",
        )
        assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.workspaces.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.workspaces.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.workspaces.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.workspaces.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.agents.evaluation_metrics.workspaces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            description="example string",
            name="example name",
            body_workspace_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.workspaces.with_raw_response.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.workspaces.with_streaming_response.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_workspace_uuid` but received ''"):
            client.agents.evaluation_metrics.workspaces.with_raw_response.update(
                path_workspace_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.workspaces.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.workspaces.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.agents.evaluation_metrics.workspaces.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_evaluation_test_cases(self, client: Gradient) -> None:
        workspace = client.agents.evaluation_metrics.workspaces.list_evaluation_test_cases(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceListEvaluationTestCasesResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_evaluation_test_cases(self, client: Gradient) -> None:
        response = client.agents.evaluation_metrics.workspaces.with_raw_response.list_evaluation_test_cases(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListEvaluationTestCasesResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_evaluation_test_cases(self, client: Gradient) -> None:
        with client.agents.evaluation_metrics.workspaces.with_streaming_response.list_evaluation_test_cases(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListEvaluationTestCasesResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_evaluation_test_cases(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            client.agents.evaluation_metrics.workspaces.with_raw_response.list_evaluation_test_cases(
                "",
            )


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.create()
        assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.create(
            agent_uuids=["example string"],
            description="example string",
            name="example name",
        )
        assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceCreateResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.with_raw_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.with_streaming_response.retrieve(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.workspaces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
            description="example string",
            name="example name",
            body_workspace_uuid="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.with_raw_response.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.with_streaming_response.update(
            path_workspace_uuid='"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceUpdateResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_workspace_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.workspaces.with_raw_response.update(
                path_workspace_uuid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.with_raw_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.with_streaming_response.delete(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.workspaces.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_evaluation_test_cases(self, async_client: AsyncGradient) -> None:
        workspace = await async_client.agents.evaluation_metrics.workspaces.list_evaluation_test_cases(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )
        assert_matches_type(WorkspaceListEvaluationTestCasesResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_evaluation_test_cases(self, async_client: AsyncGradient) -> None:
        response = await async_client.agents.evaluation_metrics.workspaces.with_raw_response.list_evaluation_test_cases(
            '"123e4567-e89b-12d3-a456-426614174000"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListEvaluationTestCasesResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_evaluation_test_cases(self, async_client: AsyncGradient) -> None:
        async with async_client.agents.evaluation_metrics.workspaces.with_streaming_response.list_evaluation_test_cases(
            '"123e4567-e89b-12d3-a456-426614174000"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListEvaluationTestCasesResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_evaluation_test_cases(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_uuid` but received ''"):
            await async_client.agents.evaluation_metrics.workspaces.with_raw_response.list_evaluation_test_cases(
                "",
            )
