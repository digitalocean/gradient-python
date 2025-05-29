# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    audio_generate_speech_params,
    audio_translate_audio_params,
    audio_transcribe_audio_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.voice_ids_shared_param import VoiceIDsSharedParam
from ..types.audio_translate_audio_response import AudioTranslateAudioResponse
from ..types.audio_transcribe_audio_response import AudioTranscribeAudioResponse

__all__ = ["AudioResource", "AsyncAudioResource"]


class AudioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AudioResourceWithStreamingResponse(self)

    def generate_speech(
        self,
        *,
        input: str,
        model: Union[str, Literal["tts-1", "tts-1-hd", "gpt-4o-mini-tts"]],
        voice: VoiceIDsSharedParam,
        instructions: str | NotGiven = NOT_GIVEN,
        response_format: Literal["mp3", "opus", "aac", "flac", "wav", "pcm"] | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Generates audio from the input text.

        Args:
          input: The text to generate audio for. The maximum length is 4096 characters.

          model: One of the available [TTS models](/docs/models#tts): `tts-1`, `tts-1-hd` or
              `gpt-4o-mini-tts`.

          voice: The voice to use when generating the audio. Supported voices are `alloy`, `ash`,
              `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, and
              `verse`. Previews of the voices are available in the
              [Text to speech guide](/docs/guides/text-to-speech#voice-options).

          instructions: Control the voice of your generated audio with additional instructions. Does not
              work with `tts-1` or `tts-1-hd`.

          response_format: The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`,
              `wav`, and `pcm`.

          speed: The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
              the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/audio/speech",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "voice": voice,
                    "instructions": instructions,
                    "response_format": response_format,
                    "speed": speed,
                },
                audio_generate_speech_params.AudioGenerateSpeechParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def transcribe_audio(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["whisper-1", "gpt-4o-transcribe", "gpt-4o-mini-transcribe"]],
        include: List[Literal["logprobs"]] | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        timestamp_granularities: List[Literal["word", "segment"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTranscribeAudioResponse:
        """
        Transcribes audio into the input language.

        Args:
          file:
              The audio file object (not file name) to transcribe, in one of these formats:
              flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          model: ID of the model to use. The options are `gpt-4o-transcribe`,
              `gpt-4o-mini-transcribe`, and `whisper-1` (which is powered by our open source
              Whisper V2 model).

          include: Additional information to include in the transcription response. `logprobs` will
              return the log probabilities of the tokens in the response to understand the
              model's confidence in the transcription. `logprobs` only works with
              response_format set to `json` and only with the models `gpt-4o-transcribe` and
              `gpt-4o-mini-transcribe`.

          language: The language of the input audio. Supplying the input language in
              [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`)
              format will improve accuracy and latency.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment. The [prompt](/docs/guides/speech-to-text#prompting) should match the
              audio language.

          response_format: The format of the output, in one of these options: `json`, `text`, `srt`,
              `verbose_json`, or `vtt`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`,
              the only supported format is `json`.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section of the Speech-to-Text guide](/docs/guides/speech-to-text?lang=curl#streaming-transcriptions)
              for more information.

              Note: Streaming is not supported for the `whisper-1` model and will be ignored.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          timestamp_granularities: The timestamp granularities to populate for this transcription.
              `response_format` must be set `verbose_json` to use timestamp granularities.
              Either or both of these options are supported: `word`, or `segment`. Note: There
              is no additional latency for segment timestamps, but generating word timestamps
              incurs additional latency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
                "include": include,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "stream": stream,
                "temperature": temperature,
                "timestamp_granularities": timestamp_granularities,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            AudioTranscribeAudioResponse,
            self._post(
                "/audio/transcriptions",
                body=maybe_transform(body, audio_transcribe_audio_params.AudioTranscribeAudioParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AudioTranscribeAudioResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def translate_audio(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["whisper-1"]],
        prompt: str | NotGiven = NOT_GIVEN,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTranslateAudioResponse:
        """
        Translates audio into English.

        Args:
          file: The audio file object (not file name) translate, in one of these formats: flac,
              mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          model: ID of the model to use. Only `whisper-1` (which is powered by our open source
              Whisper V2 model) is currently available.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment. The [prompt](/docs/guides/speech-to-text#prompting) should be in
              English.

          response_format: The format of the output, in one of these options: `json`, `text`, `srt`,
              `verbose_json`, or `vtt`.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            AudioTranslateAudioResponse,
            self._post(
                "/audio/translations",
                body=maybe_transform(body, audio_translate_audio_params.AudioTranslateAudioParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AudioTranslateAudioResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAudioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/digitalocean-genai-sdk-python#with_streaming_response
        """
        return AsyncAudioResourceWithStreamingResponse(self)

    async def generate_speech(
        self,
        *,
        input: str,
        model: Union[str, Literal["tts-1", "tts-1-hd", "gpt-4o-mini-tts"]],
        voice: VoiceIDsSharedParam,
        instructions: str | NotGiven = NOT_GIVEN,
        response_format: Literal["mp3", "opus", "aac", "flac", "wav", "pcm"] | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Generates audio from the input text.

        Args:
          input: The text to generate audio for. The maximum length is 4096 characters.

          model: One of the available [TTS models](/docs/models#tts): `tts-1`, `tts-1-hd` or
              `gpt-4o-mini-tts`.

          voice: The voice to use when generating the audio. Supported voices are `alloy`, `ash`,
              `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, and
              `verse`. Previews of the voices are available in the
              [Text to speech guide](/docs/guides/text-to-speech#voice-options).

          instructions: Control the voice of your generated audio with additional instructions. Does not
              work with `tts-1` or `tts-1-hd`.

          response_format: The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`,
              `wav`, and `pcm`.

          speed: The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
              the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/audio/speech",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "voice": voice,
                    "instructions": instructions,
                    "response_format": response_format,
                    "speed": speed,
                },
                audio_generate_speech_params.AudioGenerateSpeechParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def transcribe_audio(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["whisper-1", "gpt-4o-transcribe", "gpt-4o-mini-transcribe"]],
        include: List[Literal["logprobs"]] | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        prompt: str | NotGiven = NOT_GIVEN,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        timestamp_granularities: List[Literal["word", "segment"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTranscribeAudioResponse:
        """
        Transcribes audio into the input language.

        Args:
          file:
              The audio file object (not file name) to transcribe, in one of these formats:
              flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          model: ID of the model to use. The options are `gpt-4o-transcribe`,
              `gpt-4o-mini-transcribe`, and `whisper-1` (which is powered by our open source
              Whisper V2 model).

          include: Additional information to include in the transcription response. `logprobs` will
              return the log probabilities of the tokens in the response to understand the
              model's confidence in the transcription. `logprobs` only works with
              response_format set to `json` and only with the models `gpt-4o-transcribe` and
              `gpt-4o-mini-transcribe`.

          language: The language of the input audio. Supplying the input language in
              [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`)
              format will improve accuracy and latency.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment. The [prompt](/docs/guides/speech-to-text#prompting) should match the
              audio language.

          response_format: The format of the output, in one of these options: `json`, `text`, `srt`,
              `verbose_json`, or `vtt`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`,
              the only supported format is `json`.

          stream: If set to true, the model response data will be streamed to the client as it is
              generated using
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
              See the
              [Streaming section of the Speech-to-Text guide](/docs/guides/speech-to-text?lang=curl#streaming-transcriptions)
              for more information.

              Note: Streaming is not supported for the `whisper-1` model and will be ignored.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          timestamp_granularities: The timestamp granularities to populate for this transcription.
              `response_format` must be set `verbose_json` to use timestamp granularities.
              Either or both of these options are supported: `word`, or `segment`. Note: There
              is no additional latency for segment timestamps, but generating word timestamps
              incurs additional latency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
                "include": include,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "stream": stream,
                "temperature": temperature,
                "timestamp_granularities": timestamp_granularities,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            AudioTranscribeAudioResponse,
            await self._post(
                "/audio/transcriptions",
                body=await async_maybe_transform(body, audio_transcribe_audio_params.AudioTranscribeAudioParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AudioTranscribeAudioResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def translate_audio(
        self,
        *,
        file: FileTypes,
        model: Union[str, Literal["whisper-1"]],
        prompt: str | NotGiven = NOT_GIVEN,
        response_format: Literal["json", "text", "srt", "verbose_json", "vtt"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTranslateAudioResponse:
        """
        Translates audio into English.

        Args:
          file: The audio file object (not file name) translate, in one of these formats: flac,
              mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          model: ID of the model to use. Only `whisper-1` (which is powered by our open source
              Whisper V2 model) is currently available.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment. The [prompt](/docs/guides/speech-to-text#prompting) should be in
              English.

          response_format: The format of the output, in one of these options: `json`, `text`, `srt`,
              `verbose_json`, or `vtt`.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "model": model,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return cast(
            AudioTranslateAudioResponse,
            await self._post(
                "/audio/translations",
                body=await async_maybe_transform(body, audio_translate_audio_params.AudioTranslateAudioParams),
                files=files,
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AudioTranslateAudioResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AudioResourceWithRawResponse:
    def __init__(self, audio: AudioResource) -> None:
        self._audio = audio

        self.generate_speech = to_custom_raw_response_wrapper(
            audio.generate_speech,
            BinaryAPIResponse,
        )
        self.transcribe_audio = to_raw_response_wrapper(
            audio.transcribe_audio,
        )
        self.translate_audio = to_raw_response_wrapper(
            audio.translate_audio,
        )


class AsyncAudioResourceWithRawResponse:
    def __init__(self, audio: AsyncAudioResource) -> None:
        self._audio = audio

        self.generate_speech = async_to_custom_raw_response_wrapper(
            audio.generate_speech,
            AsyncBinaryAPIResponse,
        )
        self.transcribe_audio = async_to_raw_response_wrapper(
            audio.transcribe_audio,
        )
        self.translate_audio = async_to_raw_response_wrapper(
            audio.translate_audio,
        )


class AudioResourceWithStreamingResponse:
    def __init__(self, audio: AudioResource) -> None:
        self._audio = audio

        self.generate_speech = to_custom_streamed_response_wrapper(
            audio.generate_speech,
            StreamedBinaryAPIResponse,
        )
        self.transcribe_audio = to_streamed_response_wrapper(
            audio.transcribe_audio,
        )
        self.translate_audio = to_streamed_response_wrapper(
            audio.translate_audio,
        )


class AsyncAudioResourceWithStreamingResponse:
    def __init__(self, audio: AsyncAudioResource) -> None:
        self._audio = audio

        self.generate_speech = async_to_custom_streamed_response_wrapper(
            audio.generate_speech,
            AsyncStreamedBinaryAPIResponse,
        )
        self.transcribe_audio = async_to_streamed_response_wrapper(
            audio.transcribe_audio,
        )
        self.translate_audio = async_to_streamed_response_wrapper(
            audio.translate_audio,
        )
