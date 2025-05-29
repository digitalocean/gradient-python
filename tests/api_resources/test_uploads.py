# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types import (
    Upload,
    UploadAddPartResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        upload = client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.uploads.with_raw_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.uploads.with_streaming_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_part(self, client: DigitaloceanGenaiSDK) -> None:
        upload = client.uploads.add_part(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )
        assert_matches_type(UploadAddPartResponse, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_part(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.uploads.with_raw_response.add_part(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadAddPartResponse, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_part(self, client: DigitaloceanGenaiSDK) -> None:
        with client.uploads.with_streaming_response.add_part(
            upload_id="upload_abc123",
            data=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadAddPartResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_add_part(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.add_part(
                upload_id="",
                data=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        upload = client.uploads.cancel(
            "upload_abc123",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.uploads.with_raw_response.cancel(
            "upload_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        with client.uploads.with_streaming_response.cancel(
            "upload_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_complete(self, client: DigitaloceanGenaiSDK) -> None:
        upload = client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_complete_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        upload = client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
            md5="md5",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_complete(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.uploads.with_raw_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_complete(self, client: DigitaloceanGenaiSDK) -> None:
        with client.uploads.with_streaming_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_complete(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.complete(
                upload_id="",
                part_ids=["string"],
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        upload = await async_client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.uploads.with_raw_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.uploads.with_streaming_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_part(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        upload = await async_client.uploads.add_part(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )
        assert_matches_type(UploadAddPartResponse, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_part(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.uploads.with_raw_response.add_part(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadAddPartResponse, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_part(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.uploads.with_streaming_response.add_part(
            upload_id="upload_abc123",
            data=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadAddPartResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_add_part(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.add_part(
                upload_id="",
                data=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        upload = await async_client.uploads.cancel(
            "upload_abc123",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.uploads.with_raw_response.cancel(
            "upload_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.uploads.with_streaming_response.cancel(
            "upload_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_complete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        upload = await async_client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        upload = await async_client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
            md5="md5",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.uploads.with_raw_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.uploads.with_streaming_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.complete(
                upload_id="",
                part_ids=["string"],
            )
