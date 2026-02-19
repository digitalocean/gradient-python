# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types import BillingListInsightsResponse
from gradient._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_insights(self, client: Gradient) -> None:
        billing = client.billing.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
        )
        assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_insights_with_all_params(self, client: Gradient) -> None:
        billing = client.billing.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
            page=1,
            per_page=1,
        )
        assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_insights(self, client: Gradient) -> None:
        response = client.billing.with_raw_response.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_insights(self, client: Gradient) -> None:
        with client.billing.with_streaming_response.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_insights(self, client: Gradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_urn` but received ''"):
            client.billing.with_raw_response.list_insights(
                end_date=parse_date("2025-01-31"),
                account_urn="",
                start_date=parse_date("2025-01-01"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `start_date` but received ''"):
            client.billing.with_raw_response.list_insights(
                end_date=parse_date("2025-01-31"),
                account_urn="do:team:12345678-1234-1234-1234-123456789012",
                start_date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `end_date` but received ''"):
            client.billing.with_raw_response.list_insights(
                end_date="",
                account_urn="do:team:12345678-1234-1234-1234-123456789012",
                start_date=parse_date("2025-01-01"),
            )


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_insights(self, async_client: AsyncGradient) -> None:
        billing = await async_client.billing.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
        )
        assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_insights_with_all_params(self, async_client: AsyncGradient) -> None:
        billing = await async_client.billing.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
            page=1,
            per_page=1,
        )
        assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_insights(self, async_client: AsyncGradient) -> None:
        response = await async_client.billing.with_raw_response.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_insights(self, async_client: AsyncGradient) -> None:
        async with async_client.billing.with_streaming_response.list_insights(
            end_date=parse_date("2025-01-31"),
            account_urn="do:team:12345678-1234-1234-1234-123456789012",
            start_date=parse_date("2025-01-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingListInsightsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_insights(self, async_client: AsyncGradient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_urn` but received ''"):
            await async_client.billing.with_raw_response.list_insights(
                end_date=parse_date("2025-01-31"),
                account_urn="",
                start_date=parse_date("2025-01-01"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `start_date` but received ''"):
            await async_client.billing.with_raw_response.list_insights(
                end_date=parse_date("2025-01-31"),
                account_urn="do:team:12345678-1234-1234-1234-123456789012",
                start_date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `end_date` but received ''"):
            await async_client.billing.with_raw_response.list_insights(
                end_date="",
                account_urn="do:team:12345678-1234-1234-1234-123456789012",
                start_date=parse_date("2025-01-01"),
            )
