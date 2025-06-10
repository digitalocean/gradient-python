# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types.threads import (
    MessageObject,
    MessageListResponse,
    MessageDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.create(
            thread_id="thread_id",
            content="string",
            role="user",
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.create(
            thread_id="thread_id",
            content="string",
            role="user",
            attachments=[
                {
                    "file_id": "file_id",
                    "tools": [{"type": "code_interpreter"}],
                }
            ],
            metadata={"foo": "string"},
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.messages.with_raw_response.create(
            thread_id="thread_id",
            content="string",
            role="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.messages.with_streaming_response.create(
            thread_id="thread_id",
            content="string",
            role="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageObject, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.messages.with_raw_response.create(
                thread_id="",
                content="string",
                role="user",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.retrieve(
            message_id="message_id",
            thread_id="thread_id",
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.messages.with_raw_response.retrieve(
            message_id="message_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.messages.with_streaming_response.retrieve(
            message_id="message_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageObject, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.messages.with_raw_response.retrieve(
                message_id="message_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.threads.messages.with_raw_response.retrieve(
                message_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.update(
            message_id="message_id",
            thread_id="thread_id",
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.update(
            message_id="message_id",
            thread_id="thread_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.messages.with_raw_response.update(
            message_id="message_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.messages.with_streaming_response.update(
            message_id="message_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageObject, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.messages.with_raw_response.update(
                message_id="message_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.threads.messages.with_raw_response.update(
                message_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.list(
            thread_id="thread_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.list(
            thread_id="thread_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            run_id="run_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.messages.with_raw_response.list(
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.messages.with_streaming_response.list(
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.messages.with_raw_response.list(
                thread_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: ServerlessInferenceSDKProd) -> None:
        message = client.threads.messages.delete(
            message_id="message_id",
            thread_id="thread_id",
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.messages.with_raw_response.delete(
            message_id="message_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.messages.with_streaming_response.delete(
            message_id="message_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.messages.with_raw_response.delete(
                message_id="message_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.threads.messages.with_raw_response.delete(
                message_id="",
                thread_id="thread_id",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.create(
            thread_id="thread_id",
            content="string",
            role="user",
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.create(
            thread_id="thread_id",
            content="string",
            role="user",
            attachments=[
                {
                    "file_id": "file_id",
                    "tools": [{"type": "code_interpreter"}],
                }
            ],
            metadata={"foo": "string"},
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.messages.with_raw_response.create(
            thread_id="thread_id",
            content="string",
            role="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.messages.with_streaming_response.create(
            thread_id="thread_id",
            content="string",
            role="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageObject, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.messages.with_raw_response.create(
                thread_id="",
                content="string",
                role="user",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.retrieve(
            message_id="message_id",
            thread_id="thread_id",
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.messages.with_raw_response.retrieve(
            message_id="message_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.messages.with_streaming_response.retrieve(
            message_id="message_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageObject, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.messages.with_raw_response.retrieve(
                message_id="message_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.threads.messages.with_raw_response.retrieve(
                message_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.update(
            message_id="message_id",
            thread_id="thread_id",
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.update(
            message_id="message_id",
            thread_id="thread_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.messages.with_raw_response.update(
            message_id="message_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageObject, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.messages.with_streaming_response.update(
            message_id="message_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageObject, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.messages.with_raw_response.update(
                message_id="message_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.threads.messages.with_raw_response.update(
                message_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.list(
            thread_id="thread_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.list(
            thread_id="thread_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
            run_id="run_id",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.messages.with_raw_response.list(
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.messages.with_streaming_response.list(
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.messages.with_raw_response.list(
                thread_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        message = await async_client.threads.messages.delete(
            message_id="message_id",
            thread_id="thread_id",
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.messages.with_raw_response.delete(
            message_id="message_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.messages.with_streaming_response.delete(
            message_id="message_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.messages.with_raw_response.delete(
                message_id="message_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.threads.messages.with_raw_response.delete(
                message_id="",
                thread_id="thread_id",
            )
