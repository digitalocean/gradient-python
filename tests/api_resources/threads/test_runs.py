# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types.threads import (
    RunObject,
    RunListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.create(
            assistant_id="assistant_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.create(
            assistant_id="assistant_id",
            instructions="instructions",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            stream=True,
            temperature=1,
            thread={
                "messages": [
                    {
                        "content": "string",
                        "role": "user",
                        "attachments": [
                            {
                                "file_id": "file_id",
                                "tools": [{"type": "code_interpreter"}],
                            }
                        ],
                        "metadata": {"foo": "string"},
                    }
                ],
                "metadata": {"foo": "string"},
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["string"]},
                    "file_search": {
                        "vector_store_ids": ["string"],
                        "vector_stores": [
                            {
                                "chunking_strategy": {"type": "auto"},
                                "file_ids": ["string"],
                                "metadata": {"foo": "string"},
                            }
                        ],
                    },
                },
            },
            tool_choice="none",
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.create(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.create(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.retrieve(
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.retrieve(
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.retrieve(
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.runs.with_raw_response.retrieve(
                run_id="run_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.threads.runs.with_raw_response.retrieve(
                run_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.update(
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.update(
            run_id="run_id",
            thread_id="thread_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.update(
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.update(
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.runs.with_raw_response.update(
                run_id="run_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.threads.runs.with_raw_response.update(
                run_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.list(
            thread_id="thread_id",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.list(
            thread_id="thread_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.list(
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.list(
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.runs.with_raw_response.list(
                thread_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.cancel(
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.cancel(
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.cancel(
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.runs.with_raw_response.cancel(
                run_id="run_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.threads.runs.with_raw_response.cancel(
                run_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_run(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_run_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            additional_instructions="additional_instructions",
            additional_messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {"foo": "string"},
                }
            ],
            instructions="instructions",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            reasoning_effort="low",
            response_format="auto",
            stream=True,
            temperature=1,
            tool_choice="none",
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_run(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_run(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_run(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.runs.with_raw_response.create_run(
                thread_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_submit_tool_outputs(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_submit_tool_outputs_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        run = client.threads.runs.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[
                {
                    "output": "output",
                    "tool_call_id": "tool_call_id",
                }
            ],
            stream=True,
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_submit_tool_outputs(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.threads.runs.with_raw_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_submit_tool_outputs(self, client: ServerlessInferenceSDKProd) -> None:
        with client.threads.runs.with_streaming_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_submit_tool_outputs(self, client: ServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.threads.runs.with_raw_response.submit_tool_outputs(
                run_id="run_id",
                thread_id="",
                tool_outputs=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.threads.runs.with_raw_response.submit_tool_outputs(
                run_id="",
                thread_id="thread_id",
                tool_outputs=[{}],
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.create(
            assistant_id="assistant_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.create(
            assistant_id="assistant_id",
            instructions="instructions",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            stream=True,
            temperature=1,
            thread={
                "messages": [
                    {
                        "content": "string",
                        "role": "user",
                        "attachments": [
                            {
                                "file_id": "file_id",
                                "tools": [{"type": "code_interpreter"}],
                            }
                        ],
                        "metadata": {"foo": "string"},
                    }
                ],
                "metadata": {"foo": "string"},
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["string"]},
                    "file_search": {
                        "vector_store_ids": ["string"],
                        "vector_stores": [
                            {
                                "chunking_strategy": {"type": "auto"},
                                "file_ids": ["string"],
                                "metadata": {"foo": "string"},
                            }
                        ],
                    },
                },
            },
            tool_choice="none",
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.create(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.create(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.retrieve(
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.retrieve(
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.retrieve(
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.runs.with_raw_response.retrieve(
                run_id="run_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.threads.runs.with_raw_response.retrieve(
                run_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.update(
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.update(
            run_id="run_id",
            thread_id="thread_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.update(
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.update(
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.runs.with_raw_response.update(
                run_id="run_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.threads.runs.with_raw_response.update(
                run_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.list(
            thread_id="thread_id",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.list(
            thread_id="thread_id",
            after="after",
            before="before",
            limit=0,
            order="asc",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.list(
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.list(
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.runs.with_raw_response.list(
                thread_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.cancel(
            run_id="run_id",
            thread_id="thread_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.cancel(
            run_id="run_id",
            thread_id="thread_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.cancel(
            run_id="run_id",
            thread_id="thread_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.runs.with_raw_response.cancel(
                run_id="run_id",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.threads.runs.with_raw_response.cancel(
                run_id="",
                thread_id="thread_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_run(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_run_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            additional_instructions="additional_instructions",
            additional_messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {"foo": "string"},
                }
            ],
            instructions="instructions",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={"foo": "string"},
            model="gpt-4o",
            parallel_tool_calls=True,
            reasoning_effort="low",
            response_format="auto",
            stream=True,
            temperature=1,
            tool_choice="none",
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_run(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_run(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_run(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.runs.with_raw_response.create_run(
                thread_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_submit_tool_outputs(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        run = await async_client.threads.runs.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_submit_tool_outputs_with_all_params(
        self, async_client: AsyncServerlessInferenceSDKProd
    ) -> None:
        run = await async_client.threads.runs.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[
                {
                    "output": "output",
                    "tool_call_id": "tool_call_id",
                }
            ],
            stream=True,
        )
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_submit_tool_outputs(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.threads.runs.with_raw_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunObject, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_submit_tool_outputs(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.threads.runs.with_streaming_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunObject, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_submit_tool_outputs(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.threads.runs.with_raw_response.submit_tool_outputs(
                run_id="run_id",
                thread_id="",
                tool_outputs=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.threads.runs.with_raw_response.submit_tool_outputs(
                run_id="",
                thread_id="thread_id",
                tool_outputs=[{}],
            )
