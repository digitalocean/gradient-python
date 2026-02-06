# Tests for Responses API (client.responses.create). Use respx only; no real API.

from __future__ import annotations

import os
import json
from typing import Any

import httpx
import pytest
from respx import MockRouter

from gradient import Gradient, AsyncGradient
from tests.utils import assert_matches_type
from gradient.types.responses import ResponseCreateResponse, ResponseInputUserMessage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

# Minimal valid response body for POST /v1/responses
MINIMAL_RESPONSE_BODY: dict[str, Any] = {
    "id": "resp_123",
    "output": [],
    "status": "completed",
    "model": "openai-gpt-5.2-pro",
}

# Minimal input for create() (typed so pyright accepts as Iterable[ResponseInputItem])
MINIMAL_INPUT: list[ResponseInputUserMessage] = [
    {"type": "message", "role": "user", "content": "Hello"},
]


class TestResponsesCreateSync:
    @pytest.mark.respx(base_url=base_url)
    def test_create_minimal(self, respx_mock: MockRouter, client: Gradient) -> None:
        respx_mock.post("/v1/responses").mock(return_value=httpx.Response(200, json=MINIMAL_RESPONSE_BODY))
        resp = client.responses.create(
            model="openai-gpt-5.2-pro",
            input=MINIMAL_INPUT,
        )
        assert_matches_type(ResponseCreateResponse, resp, path=["response"])
        assert resp.id == "resp_123"
        assert resp.status == "completed"
        assert resp.output_text == ""

    @pytest.mark.respx(base_url=base_url)
    def test_create_with_tools_and_max_output_tokens(self, respx_mock: MockRouter, client: Gradient) -> None:
        respx_mock.post("/v1/responses").mock(return_value=httpx.Response(200, json=MINIMAL_RESPONSE_BODY))
        resp = client.responses.create(
            model="openai-gpt-5.2-pro",
            input=MINIMAL_INPUT,
            tools=[
                {
                    "type": "function",
                    "function": {"name": "get_weather", "description": "Get weather"},
                }
            ],
            max_output_tokens=512,
        )
        assert resp.id == "resp_123"
        request = respx_mock.calls.last.request
        assert request is not None
        body = json.loads(request.content)
        assert body.get("tools") is not None
        assert body.get("max_output_tokens") == 512

    @pytest.mark.respx(base_url=base_url)
    def test_with_raw_response_create(self, respx_mock: MockRouter, client: Gradient) -> None:
        respx_mock.post("/v1/responses").mock(return_value=httpx.Response(200, json=MINIMAL_RESPONSE_BODY))
        raw = client.responses.with_raw_response.create(
            model="openai-gpt-5.2-pro",
            input=MINIMAL_INPUT,
        )
        assert raw.is_closed is True
        parsed = raw.parse()
        assert_matches_type(ResponseCreateResponse, parsed, path=["response"])
        assert parsed.id == "resp_123"

    def test_missing_model_access_key_raises(self) -> None:
        with Gradient(
            base_url=base_url,
            access_token="token",
            model_access_key=None,
            agent_access_key="agent",
        ) as c:
            with pytest.raises(TypeError) as exc_info:
                c.responses.create(model="m", input=MINIMAL_INPUT)
            assert "model_access_key" in str(exc_info.value)


class TestResponsesCreateAsync:
    @pytest.mark.respx(base_url=base_url)
    async def test_create_minimal(self, respx_mock: MockRouter, async_client: AsyncGradient) -> None:
        respx_mock.post("/v1/responses").mock(return_value=httpx.Response(200, json=MINIMAL_RESPONSE_BODY))
        resp = await async_client.responses.create(
            model="openai-gpt-5.2-pro",
            input=MINIMAL_INPUT,
        )
        assert_matches_type(ResponseCreateResponse, resp, path=["response"])
        assert resp.id == "resp_123"

    @pytest.mark.respx(base_url=base_url)
    async def test_with_raw_response_create(self, respx_mock: MockRouter, async_client: AsyncGradient) -> None:
        respx_mock.post("/v1/responses").mock(return_value=httpx.Response(200, json=MINIMAL_RESPONSE_BODY))
        raw = await async_client.responses.with_raw_response.create(
            model="openai-gpt-5.2-pro",
            input=MINIMAL_INPUT,
        )
        assert raw.is_closed is True
        parsed = await raw.parse()
        assert parsed.id == "resp_123"

    async def test_missing_model_access_key_raises(self) -> None:
        async with AsyncGradient(
            base_url=base_url,
            access_token="token",
            model_access_key=None,
            agent_access_key="agent",
        ) as c:
            with pytest.raises(TypeError) as exc_info:
                await c.responses.create(model="m", input=MINIMAL_INPUT)
            assert "model_access_key" in str(exc_info.value)
