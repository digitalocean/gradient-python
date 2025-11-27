# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets import (
    ActionListResponse,
    ActionInitiateResponse,
    ActionRetrieveResponse,
    ActionBulkInitiateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.retrieve(
            action_id=36804636,
            droplet_id=3164444,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.retrieve(
            action_id=36804636,
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.retrieve(
            action_id=36804636,
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.list(
            droplet_id=3164444,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.list(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.list(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.list(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_initiate_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_initiate_with_all_params_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
            tag_name="tag_name",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_initiate_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.bulk_initiate(
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_initiate_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.bulk_initiate(
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_initiate_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_initiate_with_all_params_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
            tag_name="tag_name",
            name="Nifty New Snapshot",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_initiate_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.bulk_initiate(
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_initiate_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.bulk_initiate(
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
            backup_policy={
                "hour": 20,
                "plan": "daily",
                "weekday": "SUN",
            },
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_3(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_3(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
            backup_policy={
                "hour": 20,
                "plan": "weekly",
                "weekday": "SUN",
            },
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_3(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_3(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_4(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_4(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            image=12389723,
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_4(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_4(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_5(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_5(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            disk=True,
            size="s-2vcpu-2gb",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_5(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_5(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_6(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_6(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            image="ubuntu-20-04-x64",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_6(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_6(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_7(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_7(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            name="nifty-new-name",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_7(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_7(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_8(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_8(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            kernel=12389723,
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_8(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_8(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_overload_9(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params_overload_9(self, client: Gradient) -> None:
        action = client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            name="Nifty New Snapshot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_overload_9(self, client: Gradient) -> None:
        response = client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_overload_9(self, client: Gradient) -> None:
        with client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.retrieve(
            action_id=36804636,
            droplet_id=3164444,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.retrieve(
            action_id=36804636,
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.retrieve(
            action_id=36804636,
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.list(
            droplet_id=3164444,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.list(
            droplet_id=3164444,
            page=1,
            per_page=1,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.list(
            droplet_id=3164444,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.list(
            droplet_id=3164444,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_initiate_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_initiate_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
            tag_name="tag_name",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_initiate_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.bulk_initiate(
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_initiate_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.bulk_initiate(
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_initiate_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_initiate_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.bulk_initiate(
            type="reboot",
            tag_name="tag_name",
            name="Nifty New Snapshot",
        )
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_initiate_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.bulk_initiate(
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_initiate_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.bulk_initiate(
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionBulkInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
            backup_policy={
                "hour": 20,
                "plan": "daily",
                "weekday": "SUN",
            },
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_3(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_3(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="enable_backups",
            backup_policy={
                "hour": 20,
                "plan": "weekly",
                "weekday": "SUN",
            },
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_3(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_3(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="enable_backups",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_4(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_4(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            image=12389723,
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_4(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_4(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_5(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_5(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            disk=True,
            size="s-2vcpu-2gb",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_5(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_5(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_6(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_6(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            image="ubuntu-20-04-x64",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_6(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_6(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_7(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_7(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            name="nifty-new-name",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_7(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_7(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_8(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_8(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            kernel=12389723,
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_8(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_8(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_overload_9(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params_overload_9(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.actions.initiate(
            droplet_id=3164444,
            type="reboot",
            name="Nifty New Snapshot",
        )
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_overload_9(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.actions.with_raw_response.initiate(
            droplet_id=3164444,
            type="reboot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_overload_9(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.actions.with_streaming_response.initiate(
            droplet_id=3164444,
            type="reboot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True
