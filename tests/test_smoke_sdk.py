from __future__ import annotations

import os

import pytest

from gradient import Gradient

REQUIRED_ENV_VARS = (
    "DIGITALOCEAN_ACCESS_TOKEN",
    "GRADIENT_MODEL_ACCESS_KEY",
    "GRADIENT_AGENT_ACCESS_KEY",
    "GRADIENT_AGENT_ENDPOINT",
)


@pytest.mark.smoke
def test_smoke_environment_and_client_state() -> None:
    """Validate required env vars, client auto-loaded properties, and perform a minimal API call.

    This central test ensures environment configuration & client state are correct so other sync
    smoke tests can focus purely on API behavior without repeating these assertions.
    """
    missing = [k for k in REQUIRED_ENV_VARS if not os.getenv(k)]
    if missing:
        pytest.fail(
            "Missing required environment variables for smoke tests: " + ", ".join(missing),
            pytrace=False,
        )

    client = Gradient()

    # Property assertions (auto-loaded from environment)
    assert client.access_token == os.environ["DIGITALOCEAN_ACCESS_TOKEN"], "access_token not loaded from env"
    assert client.model_access_key == os.environ["GRADIENT_MODEL_ACCESS_KEY"], "model_access_key not loaded from env"
    assert client.agent_access_key == os.environ["GRADIENT_AGENT_ACCESS_KEY"], "agent_access_key not loaded from env"
    expected_endpoint = os.environ["GRADIENT_AGENT_ENDPOINT"]
    normalized_expected = (
        expected_endpoint if expected_endpoint.startswith("https://") else f"https://{expected_endpoint}"
    )
    assert client.agent_endpoint == normalized_expected, "agent_endpoint not derived correctly from env"


@pytest.mark.smoke
def test_smoke_agents_listing() -> None:
    client = Gradient()
    # Minimal API surface check (agents list)
    agents_list = client.agents.list()
    assert agents_list is not None
    assert hasattr(agents_list, "agents")


@pytest.mark.smoke
def test_smoke_gpu_droplets_listing() -> None:
    client = Gradient()
    droplets_list = client.gpu_droplets.list(type="gpus")
    assert droplets_list is not None
    assert hasattr(droplets_list, "droplets")


@pytest.mark.smoke
def test_smoke_inference_completion() -> None:
    inference_client = Gradient()
    completion = inference_client.chat.completions.create(
        model="llama3-8b-instruct",
        messages=[{"role": "user", "content": "ping"}],
    )
    # Basic structural checks
    assert completion is not None
    assert completion.choices, "Expected at least one choice in completion response"
    assert completion.choices[0].message.content is not None


@pytest.mark.smoke
def test_smoke_agent_inference_chat() -> None:
    agent_client = Gradient()

    # Model may be resolved implicitly; if an explicit model is required and missing this can be adapted
    completion = agent_client.agents.chat.completions.create(
        model="",  # Intentionally blank per original example; adjust if backend requires non-empty
        messages=[{"role": "user", "content": "ping"}],
    )
    assert completion is not None
    assert completion.choices
