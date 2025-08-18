# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.gpu_droplets.volumes import (
    ActionListResponse,
    ActionRetrieveResponse,
    ActionInitiateByIDResponse,
    ActionInitiateByNameResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            page=1,
            per_page=1,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.actions.with_raw_response.retrieve(
                action_id=36804636,
                volume_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            page=1,
            per_page=1,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.actions.with_raw_response.list(
                volume_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_id_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_id_with_all_params_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
            tags=["base-image", "prod"],
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_by_id_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_by_id_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_by_id_overload_1(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
                volume_id="",
                droplet_id=11612190,
                type="attach",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_id_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_id_with_all_params_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_by_id_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_by_id_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_by_id_overload_2(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
                volume_id="",
                droplet_id=11612190,
                type="attach",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_id_overload_3(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_id_with_all_params_overload_3(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_by_id_overload_3(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_by_id_overload_3(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initiate_by_id_overload_3(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
                volume_id="",
                size_gigabytes=16384,
                type="attach",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_name_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_name_with_all_params_overload_1(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
            tags=["base-image", "prod"],
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_by_name_overload_1(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_by_name_overload_1(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_name_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_by_name_with_all_params_overload_2(self, client: Gradient) -> None:
        action = client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_by_name_overload_2(self, client: Gradient) -> None:
        response = client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_by_name_overload_2(self, client: Gradient) -> None:
        with client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            page=1,
            per_page=1,
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.retrieve(
            action_id=36804636,
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.actions.with_raw_response.retrieve(
                action_id=36804636,
                volume_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            page=1,
            per_page=1,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.list(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.actions.with_raw_response.list(
                volume_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_id_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_id_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
            tags=["base-image", "prod"],
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_by_id_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_by_id_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_by_id_overload_1(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
                volume_id="",
                droplet_id=11612190,
                type="attach",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_id_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_id_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_by_id_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_by_id_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_by_id_overload_2(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
                volume_id="",
                droplet_id=11612190,
                type="attach",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_id_overload_3(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_id_with_all_params_overload_3(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_by_id_overload_3(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_by_id_overload_3(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_id(
            volume_id="7724db7c-e098-11e5-b522-000f53304e51",
            size_gigabytes=16384,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateByIDResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initiate_by_id_overload_3(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_id(
                volume_id="",
                size_gigabytes=16384,
                type="attach",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_name_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_name_with_all_params_overload_1(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
            tags=["base-image", "prod"],
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_by_name_overload_1(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_by_name_overload_1(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_name_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_by_name_with_all_params_overload_2(self, async_client: AsyncGradient) -> None:
        action = await async_client.gpu_droplets.volumes.actions.initiate_by_name(
            droplet_id=11612190,
            type="attach",
            page=1,
            per_page=1,
            region="nyc3",
        )
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_by_name_overload_2(self, async_client: AsyncGradient) -> None:
        response = await async_client.gpu_droplets.volumes.actions.with_raw_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_by_name_overload_2(self, async_client: AsyncGradient) -> None:
        async with async_client.gpu_droplets.volumes.actions.with_streaming_response.initiate_by_name(
            droplet_id=11612190,
            type="attach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionInitiateByNameResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True
