"""Tests for Responses API model constants."""

import pytest

from gradient import ResponsesModels


def test_responses_models_gpt_5_2_pro() -> None:
    assert ResponsesModels.GPT_5_2_PRO == "openai-gpt-5.2-pro"


def test_responses_models_gpt_5_1_codex_max() -> None:
    assert ResponsesModels.GPT_5_1_CODEX_MAX == "openai-gpt-5.1-codex-max"


def test_responses_models_constants_are_strings() -> None:
    assert isinstance(ResponsesModels.GPT_5_2_PRO, str)
    assert isinstance(ResponsesModels.GPT_5_1_CODEX_MAX, str)
