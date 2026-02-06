# Tests for Responses API response types. No network; static payloads only.

from __future__ import annotations

from gradient.types.responses import (
    ResponseOutputMessage,
    ResponseCreateResponse,
    ResponseOutputFunctionCall,
)

# Minimal valid response payload (static, no network).
MINIMAL_RESPONSE = {
    "id": "resp_123",
    "output": [],
    "status": "completed",
    "model": "openai-gpt-5.2-pro",
}


class TestResponseCreateResponseParse:
    """Test that ResponseCreateResponse parses minimal and extended JSON."""

    def test_parse_minimal_response(self) -> None:
        parsed = ResponseCreateResponse.model_validate(MINIMAL_RESPONSE)
        assert parsed.id == "resp_123"
        assert parsed.output == []
        assert parsed.status == "completed"
        assert parsed.model == "openai-gpt-5.2-pro"
        assert parsed.output_text == ""

    def test_parse_response_with_usage(self) -> None:
        payload = {
            **MINIMAL_RESPONSE,
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 5,
                "total_tokens": 15,
            },
        }
        parsed = ResponseCreateResponse.model_validate(payload)
        assert parsed.usage is not None
        assert parsed.usage.prompt_tokens == 10
        assert parsed.usage.completion_tokens == 5
        assert parsed.usage.total_tokens == 15


class TestResponseCreateResponseOutputText:
    """Test that output_text aggregates text from message items in output."""

    def test_output_text_aggregates_content(self) -> None:
        payload = {
            **MINIMAL_RESPONSE,
            "output": [
                {"type": "message", "role": "assistant", "content": "Hello "},
                {"type": "message", "role": "assistant", "content": "world."},
            ],
        }
        parsed = ResponseCreateResponse.model_validate(payload)
        assert parsed.output_text == "Hello world."

    def test_output_text_prefers_output_text_field(self) -> None:
        payload = {
            **MINIMAL_RESPONSE,
            "output": [
                {
                    "type": "message",
                    "role": "assistant",
                    "content": "raw",
                    "output_text": "aggregated",
                },
            ],
        }
        parsed = ResponseCreateResponse.model_validate(payload)
        assert parsed.output_text == "aggregated"

    def test_output_text_skips_function_call_items(self) -> None:
        payload = {
            **MINIMAL_RESPONSE,
            "output": [
                {"type": "message", "role": "assistant", "content": "Here is "},
                {
                    "type": "function_call",
                    "id": "call_1",
                    "name": "get_weather",
                    "arguments": "{}",
                },
                {"type": "message", "role": "assistant", "content": "the result."},
            ],
        }
        parsed = ResponseCreateResponse.model_validate(payload)
        assert parsed.output_text == "Here is the result."

    def test_output_text_empty_message_content_treated_as_empty(self) -> None:
        payload = {
            **MINIMAL_RESPONSE,
            "output": [
                {"type": "message", "role": "assistant", "content": None},
                {"type": "message", "role": "assistant", "output_text": "only this"},
            ],
        }
        parsed = ResponseCreateResponse.model_validate(payload)
        assert parsed.output_text == "only this"


class TestResponseOutputItemTypes:
    """Test that output item types parse correctly."""

    def test_message_item_parses(self) -> None:
        msg = ResponseOutputMessage.model_validate({"type": "message", "role": "assistant", "content": "Hi"})
        assert msg.type == "message"
        assert msg.role == "assistant"
        assert msg.content == "Hi"

    def test_function_call_item_parses(self) -> None:
        fc = ResponseOutputFunctionCall.model_validate(
            {
                "type": "function_call",
                "id": "call_1",
                "name": "foo",
                "arguments": '{"x": 1}',
            }
        )
        assert fc.type == "function_call"
        assert fc.id == "call_1"
        assert fc.name == "foo"
        assert fc.arguments == '{"x": 1}'
