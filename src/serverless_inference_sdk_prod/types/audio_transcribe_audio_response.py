# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .transcription_segment import TranscriptionSegment

__all__ = [
    "AudioTranscribeAudioResponse",
    "CreateTranscriptionResponseJson",
    "CreateTranscriptionResponseJsonLogprob",
    "CreateTranscriptionResponseVerboseJson",
    "CreateTranscriptionResponseVerboseJsonWord",
]


class CreateTranscriptionResponseJsonLogprob(BaseModel):
    token: str
    """The token that was used to generate the log probability."""

    bytes: List[int]
    """The bytes that were used to generate the log probability."""

    logprob: float
    """The log probability of the token."""


class CreateTranscriptionResponseJson(BaseModel):
    text: str
    """The transcribed text."""

    logprobs: Optional[List[CreateTranscriptionResponseJsonLogprob]] = None
    """The log probabilities of the tokens in the transcription.

    Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`
    if `logprobs` is added to the `include` array.
    """


class CreateTranscriptionResponseVerboseJsonWord(BaseModel):
    end: float
    """End time of the word in seconds."""

    start: float
    """Start time of the word in seconds."""

    word: str
    """The text content of the word."""


class CreateTranscriptionResponseVerboseJson(BaseModel):
    duration: float
    """The duration of the input audio."""

    language: str
    """The language of the input audio."""

    text: str
    """The transcribed text."""

    segments: Optional[List[TranscriptionSegment]] = None
    """Segments of the transcribed text and their corresponding details."""

    words: Optional[List[CreateTranscriptionResponseVerboseJsonWord]] = None
    """Extracted words and their corresponding timestamps."""


AudioTranscribeAudioResponse: TypeAlias = Union[CreateTranscriptionResponseJson, CreateTranscriptionResponseVerboseJson]
