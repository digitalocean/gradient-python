# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types import (
    OpenAIFile,
    FileListResponse,
    FileDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        file = client.files.retrieve(
            "file_id",
        )
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.files.with_raw_response.retrieve(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with client.files.with_streaming_response.retrieve(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(OpenAIFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: ServerlessInferenceSDKProd) -> None:
        file = client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        file = client.files.list(
            after="after",
            limit=0,
            order="asc",
            purpose="purpose",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: ServerlessInferenceSDKProd) -> None:
        file = client.files.delete(
            "file_id",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: ServerlessInferenceSDKProd) -> None:
        with client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_content(self, client: ServerlessInferenceSDKProd) -> None:
        file = client.files.retrieve_content(
            "file_id",
        )
        assert_matches_type(str, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_content(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.files.with_raw_response.retrieve_content(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_content(self, client: ServerlessInferenceSDKProd) -> None:
        with client.files.with_streaming_response.retrieve_content(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_content(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve_content(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: ServerlessInferenceSDKProd) -> None:
        file = client.files.upload(
            file=b"raw file contents",
            purpose="assistants",
        )
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.files.with_raw_response.upload(
            file=b"raw file contents",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: ServerlessInferenceSDKProd) -> None:
        with client.files.with_streaming_response.upload(
            file=b"raw file contents",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(OpenAIFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        file = await async_client.files.retrieve(
            "file_id",
        )
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(OpenAIFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        file = await async_client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        file = await async_client.files.list(
            after="after",
            limit=0,
            order="asc",
            purpose="purpose",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        file = await async_client.files.delete(
            "file_id",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_content(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        file = await async_client.files.retrieve_content(
            "file_id",
        )
        assert_matches_type(str, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_content(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.files.with_raw_response.retrieve_content(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(str, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_content(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.files.with_streaming_response.retrieve_content(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_content(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.retrieve_content(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
            purpose="assistants",
        )
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.files.with_raw_response.upload(
            file=b"raw file contents",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(OpenAIFile, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.files.with_streaming_response.upload(
            file=b"raw file contents",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(OpenAIFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True
