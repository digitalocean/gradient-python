# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from serverless_inference_sdk_prod import ServerlessInferenceSDKProd, AsyncServerlessInferenceSDKProd
from serverless_inference_sdk_prod.types import (
    RealtimeCreateSessionResponse,
    RealtimeCreateTranscriptionSessionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRealtime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_session(self, client: ServerlessInferenceSDKProd) -> None:
        realtime = client.realtime.create_session()
        assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_session_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        realtime = client.realtime.create_session(
            input_audio_format="pcm16",
            input_audio_noise_reduction={"type": "near_field"},
            input_audio_transcription={
                "language": "language",
                "model": "model",
                "prompt": "prompt",
            },
            instructions="instructions",
            max_response_output_tokens=0,
            modalities=["text"],
            model="gpt-4o-realtime-preview",
            output_audio_format="pcm16",
            temperature=0,
            tool_choice="tool_choice",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {},
                    "type": "function",
                }
            ],
            turn_detection={
                "create_response": True,
                "eagerness": "low",
                "interrupt_response": True,
                "prefix_padding_ms": 0,
                "silence_duration_ms": 0,
                "threshold": 0,
                "type": "server_vad",
            },
            voice="ash",
        )
        assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_session(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.realtime.with_raw_response.create_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = response.parse()
        assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_session(self, client: ServerlessInferenceSDKProd) -> None:
        with client.realtime.with_streaming_response.create_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = response.parse()
            assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_transcription_session(self, client: ServerlessInferenceSDKProd) -> None:
        realtime = client.realtime.create_transcription_session()
        assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_transcription_session_with_all_params(self, client: ServerlessInferenceSDKProd) -> None:
        realtime = client.realtime.create_transcription_session(
            include=["string"],
            input_audio_format="pcm16",
            input_audio_noise_reduction={"type": "near_field"},
            input_audio_transcription={
                "language": "language",
                "model": "gpt-4o-transcribe",
                "prompt": "prompt",
            },
            modalities=["text"],
            turn_detection={
                "create_response": True,
                "eagerness": "low",
                "interrupt_response": True,
                "prefix_padding_ms": 0,
                "silence_duration_ms": 0,
                "threshold": 0,
                "type": "server_vad",
            },
        )
        assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_transcription_session(self, client: ServerlessInferenceSDKProd) -> None:
        response = client.realtime.with_raw_response.create_transcription_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = response.parse()
        assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_transcription_session(self, client: ServerlessInferenceSDKProd) -> None:
        with client.realtime.with_streaming_response.create_transcription_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = response.parse()
            assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRealtime:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_session(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        realtime = await async_client.realtime.create_session()
        assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_session_with_all_params(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        realtime = await async_client.realtime.create_session(
            input_audio_format="pcm16",
            input_audio_noise_reduction={"type": "near_field"},
            input_audio_transcription={
                "language": "language",
                "model": "model",
                "prompt": "prompt",
            },
            instructions="instructions",
            max_response_output_tokens=0,
            modalities=["text"],
            model="gpt-4o-realtime-preview",
            output_audio_format="pcm16",
            temperature=0,
            tool_choice="tool_choice",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {},
                    "type": "function",
                }
            ],
            turn_detection={
                "create_response": True,
                "eagerness": "low",
                "interrupt_response": True,
                "prefix_padding_ms": 0,
                "silence_duration_ms": 0,
                "threshold": 0,
                "type": "server_vad",
            },
            voice="ash",
        )
        assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        response = await async_client.realtime.with_raw_response.create_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = await response.parse()
        assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        async with async_client.realtime.with_streaming_response.create_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = await response.parse()
            assert_matches_type(RealtimeCreateSessionResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_transcription_session(self, async_client: AsyncServerlessInferenceSDKProd) -> None:
        realtime = await async_client.realtime.create_transcription_session()
        assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_transcription_session_with_all_params(
        self, async_client: AsyncServerlessInferenceSDKProd
    ) -> None:
        realtime = await async_client.realtime.create_transcription_session(
            include=["string"],
            input_audio_format="pcm16",
            input_audio_noise_reduction={"type": "near_field"},
            input_audio_transcription={
                "language": "language",
                "model": "gpt-4o-transcribe",
                "prompt": "prompt",
            },
            modalities=["text"],
            turn_detection={
                "create_response": True,
                "eagerness": "low",
                "interrupt_response": True,
                "prefix_padding_ms": 0,
                "silence_duration_ms": 0,
                "threshold": 0,
                "type": "server_vad",
            },
        )
        assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_transcription_session(
        self, async_client: AsyncServerlessInferenceSDKProd
    ) -> None:
        response = await async_client.realtime.with_raw_response.create_transcription_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        realtime = await response.parse()
        assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_transcription_session(
        self, async_client: AsyncServerlessInferenceSDKProd
    ) -> None:
        async with async_client.realtime.with_streaming_response.create_transcription_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            realtime = await response.parse()
            assert_matches_type(RealtimeCreateTranscriptionSessionResponse, realtime, path=["response"])

        assert cast(Any, response.is_closed) is True
