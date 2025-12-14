# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import RetrieveDocumentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_documents(self, client: Gradient) -> None:
        retrieve = client.retrieve.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
        )
        assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_documents_with_all_params(self, client: Gradient) -> None:
        retrieve = client.retrieve.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
            alpha=0.75,
            filters={
                "must": [
                    {
                        "field": "category",
                        "operator": "eq",
                        "value": "documentation",
                    }
                ],
                "must_not": [
                    {
                        "field": "category",
                        "operator": "eq",
                        "value": "documentation",
                    }
                ],
                "should": [
                    {
                        "field": "category",
                        "operator": "eq",
                        "value": "documentation",
                    }
                ],
            },
        )
        assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_documents(self, client: Gradient) -> None:
        response = client.retrieve.with_raw_response.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieve = response.parse()
        assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_documents(self, client: Gradient) -> None:
        with client.retrieve.with_streaming_response.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieve = response.parse()
            assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_documents(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.retrieve.with_raw_response.documents(
                knowledge_base_id="",
                num_results=5,
                query="What are the best practices for deploying machine learning models?",
            )


class TestAsyncRetrieve:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_documents(self, async_client: AsyncGradient) -> None:
        retrieve = await async_client.retrieve.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
        )
        assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_documents_with_all_params(self, async_client: AsyncGradient) -> None:
        retrieve = await async_client.retrieve.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
            alpha=0.75,
            filters={
                "must": [
                    {
                        "field": "category",
                        "operator": "eq",
                        "value": "documentation",
                    }
                ],
                "must_not": [
                    {
                        "field": "category",
                        "operator": "eq",
                        "value": "documentation",
                    }
                ],
                "should": [
                    {
                        "field": "category",
                        "operator": "eq",
                        "value": "documentation",
                    }
                ],
            },
        )
        assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_documents(self, async_client: AsyncGradient) -> None:
        response = await async_client.retrieve.with_raw_response.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieve = await response.parse()
        assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_documents(self, async_client: AsyncGradient) -> None:
        async with async_client.retrieve.with_streaming_response.documents(
            knowledge_base_id="550e8400-e29b-41d4-a716-446655440000",
            num_results=5,
            query="What are the best practices for deploying machine learning models?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieve = await response.parse()
            assert_matches_type(RetrieveDocumentsResponse, retrieve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_documents(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.retrieve.with_raw_response.documents(
                knowledge_base_id="",
                num_results=5,
                query="What are the best practices for deploying machine learning models?",
            )
