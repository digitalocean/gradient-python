from __future__ import annotations

import os

import pytest

from gradient import AsyncGradient

REQUIRED_ENV_VARS = (
    "DIGITALOCEAN_ACCESS_TOKEN",
    "GRADIENT_MODEL_ACCESS_KEY",
    "GRADIENT_AGENT_ACCESS_KEY",
    "GRADIENT_AGENT_ENDPOINT",
)


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_async_smoke_environment_and_client_state() -> None:
    """Validate required env vars, client auto-loaded properties, and perform a minimal API call.

    This central test ensures environment configuration & client state are correct so other async
    smoke tests can focus purely on API behavior without repeating these assertions.
    """
    missing = [k for k in REQUIRED_ENV_VARS if not os.getenv(k)]
    if missing:
        pytest.fail(
            "Missing required environment variables for async smoke tests: " + ", ".join(missing),
            pytrace=False,
        )

    async with AsyncGradient() as client:
        # Property assertions (auto-loaded from environment)
        assert client.access_token == os.environ["DIGITALOCEAN_ACCESS_TOKEN"], "access_token not loaded from env"
        assert client.model_access_key == os.environ["GRADIENT_MODEL_ACCESS_KEY"], (
            "model_access_key not loaded from env"
        )
        assert client.agent_access_key == os.environ["GRADIENT_AGENT_ACCESS_KEY"], (
            "agent_access_key not loaded from env"
        )
        expected_endpoint = os.environ["GRADIENT_AGENT_ENDPOINT"]
        normalized_expected = (
            expected_endpoint if expected_endpoint.startswith("https://") else f"https://{expected_endpoint}"
        )
        assert client.agent_endpoint == normalized_expected, "agent_endpoint not derived correctly from env"


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_async_smoke_agents_listing() -> None:
    async with AsyncGradient() as client:
        agents_list = await client.agents.list()
        assert agents_list is not None
        assert hasattr(agents_list, "agents")


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_async_smoke_gpu_droplets_listing() -> None:
    async with AsyncGradient() as client:
        droplets_list = await client.gpu_droplets.list(type="gpus")
        assert droplets_list is not None
        assert hasattr(droplets_list, "droplets")


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_async_smoke_inference_completion() -> None:
    async with AsyncGradient() as inference_client:
        completion = await inference_client.chat.completions.create(
            model="llama3-8b-instruct",
            messages=[{"role": "user", "content": "ping"}],
        )
        assert completion is not None
        assert completion.choices
        assert completion.choices[0].message.content is not None


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_async_smoke_agent_inference_chat() -> None:
    async with AsyncGradient() as agent_client:
        completion = await agent_client.agents.chat.completions.create(
            model="",
            messages=[{"role": "user", "content": "ping"}],
        )
        assert completion is not None
        assert completion.choices
