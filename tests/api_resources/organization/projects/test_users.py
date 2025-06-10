# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types.organization.projects import (
    ProjectUser,
    UserListResponse,
    UserDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        user = client.organization.projects.users.retrieve(
            user_id="user_id",
            project_id="project_id",
        )
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.users.with_raw_response.retrieve(
            user_id="user_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.users.with_streaming_response.retrieve(
            user_id="user_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ProjectUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.users.with_raw_response.retrieve(
                user_id="user_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organization.projects.users.with_raw_response.retrieve(
                user_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: ServerlessInferenceSDKProd) -> None:
        user = client.organization.projects.users.update(
            user_id="user_id",
            project_id="project_id",
            role="owner",
        )
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.users.with_raw_response.update(
            user_id="user_id",
            project_id="project_id",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.users.with_streaming_response.update(
            user_id="user_id",
            project_id="project_id",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ProjectUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.users.with_raw_response.update(
                user_id="user_id",
                project_id="",
                role="owner",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organization.projects.users.with_raw_response.update(
                user_id="",
                project_id="project_id",
                role="owner",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: ServerlessInferenceSDKProd) -> None:
        user = client.organization.projects.users.list(
            project_id="project_id",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        user = client.organization.projects.users.list(
            project_id="project_id",
            after="after",
            limit=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.users.with_raw_response.list(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.users.with_streaming_response.list(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.users.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: ServerlessInferenceSDKProd) -> None:
        user = client.organization.projects.users.delete(
            user_id="user_id",
            project_id="project_id",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.users.with_raw_response.delete(
            user_id="user_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.users.with_streaming_response.delete(
            user_id="user_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.users.with_raw_response.delete(
                user_id="user_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organization.projects.users.with_raw_response.delete(
                user_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_add(self, client: ServerlessInferenceSDKProd) -> None:
        user = client.organization.projects.users.add(
            project_id="project_id",
            role="owner",
            user_id="user_id",
        )
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.organization.projects.users.with_raw_response.add(
            project_id="project_id",
            role="owner",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add(self, client: ServerlessInferenceSDKProd) -> None:
        with client.organization.projects.users.with_streaming_response.add(
            project_id="project_id",
            role="owner",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ProjectUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_add(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.organization.projects.users.with_raw_response.add(
                project_id="",
                role="owner",
                user_id="user_id",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        user = await async_client.organization.projects.users.retrieve(
            user_id="user_id",
            project_id="project_id",
        )
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.users.with_raw_response.retrieve(
            user_id="user_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.users.with_streaming_response.retrieve(
            user_id="user_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ProjectUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.retrieve(
                user_id="user_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.retrieve(
                user_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        user = await async_client.organization.projects.users.update(
            user_id="user_id",
            project_id="project_id",
            role="owner",
        )
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.users.with_raw_response.update(
            user_id="user_id",
            project_id="project_id",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.users.with_streaming_response.update(
            user_id="user_id",
            project_id="project_id",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ProjectUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.update(
                user_id="user_id",
                project_id="",
                role="owner",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.update(
                user_id="",
                project_id="project_id",
                role="owner",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        user = await async_client.organization.projects.users.list(
            project_id="project_id",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        user = await async_client.organization.projects.users.list(
            project_id="project_id",
            after="after",
            limit=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.users.with_raw_response.list(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.users.with_streaming_response.list(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.list(
                project_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        user = await async_client.organization.projects.users.delete(
            user_id="user_id",
            project_id="project_id",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.users.with_raw_response.delete(
            user_id="user_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.users.with_streaming_response.delete(
            user_id="user_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.delete(
                user_id="user_id",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.delete(
                user_id="",
                project_id="project_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_add(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        user = await async_client.organization.projects.users.add(
            project_id="project_id",
            role="owner",
            user_id="user_id",
        )
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.organization.projects.users.with_raw_response.add(
            project_id="project_id",
            role="owner",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ProjectUser, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.organization.projects.users.with_streaming_response.add(
            project_id="project_id",
            role="owner",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ProjectUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_add(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.organization.projects.users.with_raw_response.add(
                project_id="",
                role="owner",
                user_id="user_id",
            )
