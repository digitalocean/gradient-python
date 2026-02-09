"""
Example: Responses API with tool (function) calling

Demonstrates using client.responses.create() with a function tool: send a user
message, handle a function_call in the output, append the function result as
function_call_output, call create again, and print the final text.

Requires GRADIENT_MODEL_ACCESS_KEY in the environment (e.g. from a .env file).
"""

import os
from typing import List, cast

from gradient import Gradient, ResponsesModels
from gradient.types.responses import (
    ResponseInputFunctionCall,
    ResponseInputFunctionCallOutput,
    ResponseInputItem,
    ResponseTool,
)
from gradient.types.responses.response_create_response import ResponseOutputFunctionCall


def _load_dotenv() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore[reportMissingImports]

        load_dotenv()
    except ImportError:
        pass


_load_dotenv()

MODEL_ACCESS_KEY = os.environ.get("GRADIENT_MODEL_ACCESS_KEY")
if not MODEL_ACCESS_KEY:
    raise SystemExit("Set GRADIENT_MODEL_ACCESS_KEY in the environment to run this example.")

client = Gradient(model_access_key=MODEL_ACCESS_KEY)

# One function tool: get_weather
get_weather_tool: ResponseTool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "default": "celsius"},
            },
            "required": ["city"],
        },
    },
}

# Initial conversation: single user message
input_messages: List[ResponseInputItem] = cast(
    List[ResponseInputItem],
    [{"type": "message", "role": "user", "content": "What's the weather in New York?"}],
)

# First call: model may return a function_call
response = client.responses.create(
    model=ResponsesModels.GPT_5_1_CODEX_MAX,
    input=input_messages,
    tools=[get_weather_tool],
    tool_choice="auto",
)

# If the model returned a function call, append it and the tool result, then call again
for item in response.output:
    if isinstance(item, ResponseOutputFunctionCall):
        input_messages.append(
            cast(
                ResponseInputFunctionCall,
                {"type": "function_call", "id": item.id, "name": item.name, "arguments": item.arguments},
            )
        )
        # Simulated tool result (in a real app you would call your function here)
        input_messages.append(
            cast(
                ResponseInputFunctionCallOutput,
                {
                    "type": "function_call_output",
                    "call_id": item.id,
                    "output": '{"temperature": 22, "unit": "celsius", "conditions": "sunny"}',
                },
            )
        )
        response = client.responses.create(
            model=ResponsesModels.GPT_5_1_CODEX_MAX,
            input=input_messages,
            tools=[get_weather_tool],
            tool_choice="auto",
        )
        break

print("Assistant:", response.output_text.strip() or "(no text)")
