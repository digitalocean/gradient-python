# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import realtime_create_session_params, realtime_create_transcription_session_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.voice_ids_shared_param import VoiceIDsSharedParam
from ..types.realtime_create_session_response import RealtimeCreateSessionResponse
from ..types.realtime_create_transcription_session_response import RealtimeCreateTranscriptionSessionResponse

__all__ = ["RealtimeResource", "AsyncRealtimeResource"]


class RealtimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#accessing-raw-response-data-eg-headers
        """
        return RealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#with_streaming_response
        """
        return RealtimeResourceWithStreamingResponse(self)

    def create_session(
        self,
        *,
        input_audio_format: Literal["pcm16", "g711_ulaw", "g711_alaw"] | NotGiven = NOT_GIVEN,
        input_audio_noise_reduction: realtime_create_session_params.InputAudioNoiseReduction | NotGiven = NOT_GIVEN,
        input_audio_transcription: realtime_create_session_params.InputAudioTranscription | NotGiven = NOT_GIVEN,
        instructions: str | NotGiven = NOT_GIVEN,
        max_response_output_tokens: Union[int, Literal["inf"]] | NotGiven = NOT_GIVEN,
        modalities: List[Literal["text", "audio"]] | NotGiven = NOT_GIVEN,
        model: Literal[
            "gpt-4o-realtime-preview",
            "gpt-4o-realtime-preview-2024-10-01",
            "gpt-4o-realtime-preview-2024-12-17",
            "gpt-4o-mini-realtime-preview",
            "gpt-4o-mini-realtime-preview-2024-12-17",
        ]
        | NotGiven = NOT_GIVEN,
        output_audio_format: Literal["pcm16", "g711_ulaw", "g711_alaw"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: str | NotGiven = NOT_GIVEN,
        tools: Iterable[realtime_create_session_params.Tool] | NotGiven = NOT_GIVEN,
        turn_detection: realtime_create_session_params.TurnDetection | NotGiven = NOT_GIVEN,
        voice: VoiceIDsSharedParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeCreateSessionResponse:
        """
        Create an ephemeral API token for use in client-side applications with the
        Realtime API. Can be configured with the same session parameters as the
        `session.update` client event.

        It responds with a session object, plus a `client_secret` key which contains a
        usable ephemeral API token that can be used to authenticate browser clients for
        the Realtime API.

        Args:
          input_audio_format: The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`. For
              `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate, single channel
              (mono), and little-endian byte order.

          input_audio_noise_reduction: Configuration for input audio noise reduction. This can be set to `null` to turn
              off. Noise reduction filters audio added to the input audio buffer before it is
              sent to VAD and the model. Filtering the audio can improve VAD and turn
              detection accuracy (reducing false positives) and model performance by improving
              perception of the input audio.

          input_audio_transcription: Configuration for input audio transcription, defaults to off and can be set to
              `null` to turn off once on. Input audio transcription is not native to the
              model, since the model consumes audio directly. Transcription runs
              asynchronously through
              [the /audio/transcriptions endpoint](https://platform.openai.com/docs/api-reference/audio/createTranscription)
              and should be treated as guidance of input audio content rather than precisely
              what the model heard. The client can optionally set the language and prompt for
              transcription, these offer additional guidance to the transcription service.

          instructions: The default system instructions (i.e. system message) prepended to model calls.
              This field allows the client to guide the model on desired responses. The model
              can be instructed on response content and format, (e.g. "be extremely succinct",
              "act friendly", "here are examples of good responses") and on audio behavior
              (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The
              instructions are not guaranteed to be followed by the model, but they provide
              guidance to the model on the desired behavior.

              Note that the server sets default instructions which will be used if this field
              is not set and are visible in the `session.created` event at the start of the
              session.

          max_response_output_tokens: Maximum number of output tokens for a single assistant response, inclusive of
              tool calls. Provide an integer between 1 and 4096 to limit output tokens, or
              `inf` for the maximum available tokens for a given model. Defaults to `inf`.

          modalities: The set of modalities the model can respond with. To disable audio, set this to
              ["text"].

          model: The Realtime model used for this session.

          output_audio_format: The format of output audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`.
              For `pcm16`, output audio is sampled at a rate of 24kHz.

          temperature: Sampling temperature for the model, limited to [0.6, 1.2]. For audio models a
              temperature of 0.8 is highly recommended for best performance.

          tool_choice: How the model chooses tools. Options are `auto`, `none`, `required`, or specify
              a function.

          tools: Tools (functions) available to the model.

          turn_detection: Configuration for turn detection, ether Server VAD or Semantic VAD. This can be
              set to `null` to turn off, in which case the client must manually trigger model
              response. Server VAD means that the model will detect the start and end of
              speech based on audio volume and respond at the end of user speech. Semantic VAD
              is more advanced and uses a turn detection model (in conjuction with VAD) to
              semantically estimate whether the user has finished speaking, then dynamically
              sets a timeout based on this probability. For example, if user audio trails off
              with "uhhm", the model will score a low probability of turn end and wait longer
              for the user to continue speaking. This can be useful for more natural
              conversations, but may have a higher latency.

          voice: The voice the model uses to respond. Voice cannot be changed during the session
              once the model has responded with audio at least once. Current voice options are
              `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`,
              `shimmer`, and `verse`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/realtime/sessions",
            body=maybe_transform(
                {
                    "input_audio_format": input_audio_format,
                    "input_audio_noise_reduction": input_audio_noise_reduction,
                    "input_audio_transcription": input_audio_transcription,
                    "instructions": instructions,
                    "max_response_output_tokens": max_response_output_tokens,
                    "modalities": modalities,
                    "model": model,
                    "output_audio_format": output_audio_format,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "turn_detection": turn_detection,
                    "voice": voice,
                },
                realtime_create_session_params.RealtimeCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateSessionResponse,
        )

    def create_transcription_session(
        self,
        *,
        include: List[str] | NotGiven = NOT_GIVEN,
        input_audio_format: Literal["pcm16", "g711_ulaw", "g711_alaw"] | NotGiven = NOT_GIVEN,
        input_audio_noise_reduction: realtime_create_transcription_session_params.InputAudioNoiseReduction
        | NotGiven = NOT_GIVEN,
        input_audio_transcription: realtime_create_transcription_session_params.InputAudioTranscription
        | NotGiven = NOT_GIVEN,
        modalities: List[Literal["text", "audio"]] | NotGiven = NOT_GIVEN,
        turn_detection: realtime_create_transcription_session_params.TurnDetection | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeCreateTranscriptionSessionResponse:
        """
        Create an ephemeral API token for use in client-side applications with the
        Realtime API specifically for realtime transcriptions. Can be configured with
        the same session parameters as the `transcription_session.update` client event.

        It responds with a session object, plus a `client_secret` key which contains a
        usable ephemeral API token that can be used to authenticate browser clients for
        the Realtime API.

        Args:
          include:
              The set of items to include in the transcription. Current available items are:

              - `item.input_audio_transcription.logprobs`

          input_audio_format: The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`. For
              `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate, single channel
              (mono), and little-endian byte order.

          input_audio_noise_reduction: Configuration for input audio noise reduction. This can be set to `null` to turn
              off. Noise reduction filters audio added to the input audio buffer before it is
              sent to VAD and the model. Filtering the audio can improve VAD and turn
              detection accuracy (reducing false positives) and model performance by improving
              perception of the input audio.

          input_audio_transcription: Configuration for input audio transcription. The client can optionally set the
              language and prompt for transcription, these offer additional guidance to the
              transcription service.

          modalities: The set of modalities the model can respond with. To disable audio, set this to
              ["text"].

          turn_detection: Configuration for turn detection, ether Server VAD or Semantic VAD. This can be
              set to `null` to turn off, in which case the client must manually trigger model
              response. Server VAD means that the model will detect the start and end of
              speech based on audio volume and respond at the end of user speech. Semantic VAD
              is more advanced and uses a turn detection model (in conjuction with VAD) to
              semantically estimate whether the user has finished speaking, then dynamically
              sets a timeout based on this probability. For example, if user audio trails off
              with "uhhm", the model will score a low probability of turn end and wait longer
              for the user to continue speaking. This can be useful for more natural
              conversations, but may have a higher latency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/realtime/transcription_sessions",
            body=maybe_transform(
                {
                    "include": include,
                    "input_audio_format": input_audio_format,
                    "input_audio_noise_reduction": input_audio_noise_reduction,
                    "input_audio_transcription": input_audio_transcription,
                    "modalities": modalities,
                    "turn_detection": turn_detection,
                },
                realtime_create_transcription_session_params.RealtimeCreateTranscriptionSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateTranscriptionSessionResponse,
        )


class AsyncRealtimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/serverless-inference-sdk-prod-python#with_streaming_response
        """
        return AsyncRealtimeResourceWithStreamingResponse(self)

    async def create_session(
        self,
        *,
        input_audio_format: Literal["pcm16", "g711_ulaw", "g711_alaw"] | NotGiven = NOT_GIVEN,
        input_audio_noise_reduction: realtime_create_session_params.InputAudioNoiseReduction | NotGiven = NOT_GIVEN,
        input_audio_transcription: realtime_create_session_params.InputAudioTranscription | NotGiven = NOT_GIVEN,
        instructions: str | NotGiven = NOT_GIVEN,
        max_response_output_tokens: Union[int, Literal["inf"]] | NotGiven = NOT_GIVEN,
        modalities: List[Literal["text", "audio"]] | NotGiven = NOT_GIVEN,
        model: Literal[
            "gpt-4o-realtime-preview",
            "gpt-4o-realtime-preview-2024-10-01",
            "gpt-4o-realtime-preview-2024-12-17",
            "gpt-4o-mini-realtime-preview",
            "gpt-4o-mini-realtime-preview-2024-12-17",
        ]
        | NotGiven = NOT_GIVEN,
        output_audio_format: Literal["pcm16", "g711_ulaw", "g711_alaw"] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: str | NotGiven = NOT_GIVEN,
        tools: Iterable[realtime_create_session_params.Tool] | NotGiven = NOT_GIVEN,
        turn_detection: realtime_create_session_params.TurnDetection | NotGiven = NOT_GIVEN,
        voice: VoiceIDsSharedParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeCreateSessionResponse:
        """
        Create an ephemeral API token for use in client-side applications with the
        Realtime API. Can be configured with the same session parameters as the
        `session.update` client event.

        It responds with a session object, plus a `client_secret` key which contains a
        usable ephemeral API token that can be used to authenticate browser clients for
        the Realtime API.

        Args:
          input_audio_format: The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`. For
              `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate, single channel
              (mono), and little-endian byte order.

          input_audio_noise_reduction: Configuration for input audio noise reduction. This can be set to `null` to turn
              off. Noise reduction filters audio added to the input audio buffer before it is
              sent to VAD and the model. Filtering the audio can improve VAD and turn
              detection accuracy (reducing false positives) and model performance by improving
              perception of the input audio.

          input_audio_transcription: Configuration for input audio transcription, defaults to off and can be set to
              `null` to turn off once on. Input audio transcription is not native to the
              model, since the model consumes audio directly. Transcription runs
              asynchronously through
              [the /audio/transcriptions endpoint](https://platform.openai.com/docs/api-reference/audio/createTranscription)
              and should be treated as guidance of input audio content rather than precisely
              what the model heard. The client can optionally set the language and prompt for
              transcription, these offer additional guidance to the transcription service.

          instructions: The default system instructions (i.e. system message) prepended to model calls.
              This field allows the client to guide the model on desired responses. The model
              can be instructed on response content and format, (e.g. "be extremely succinct",
              "act friendly", "here are examples of good responses") and on audio behavior
              (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The
              instructions are not guaranteed to be followed by the model, but they provide
              guidance to the model on the desired behavior.

              Note that the server sets default instructions which will be used if this field
              is not set and are visible in the `session.created` event at the start of the
              session.

          max_response_output_tokens: Maximum number of output tokens for a single assistant response, inclusive of
              tool calls. Provide an integer between 1 and 4096 to limit output tokens, or
              `inf` for the maximum available tokens for a given model. Defaults to `inf`.

          modalities: The set of modalities the model can respond with. To disable audio, set this to
              ["text"].

          model: The Realtime model used for this session.

          output_audio_format: The format of output audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`.
              For `pcm16`, output audio is sampled at a rate of 24kHz.

          temperature: Sampling temperature for the model, limited to [0.6, 1.2]. For audio models a
              temperature of 0.8 is highly recommended for best performance.

          tool_choice: How the model chooses tools. Options are `auto`, `none`, `required`, or specify
              a function.

          tools: Tools (functions) available to the model.

          turn_detection: Configuration for turn detection, ether Server VAD or Semantic VAD. This can be
              set to `null` to turn off, in which case the client must manually trigger model
              response. Server VAD means that the model will detect the start and end of
              speech based on audio volume and respond at the end of user speech. Semantic VAD
              is more advanced and uses a turn detection model (in conjuction with VAD) to
              semantically estimate whether the user has finished speaking, then dynamically
              sets a timeout based on this probability. For example, if user audio trails off
              with "uhhm", the model will score a low probability of turn end and wait longer
              for the user to continue speaking. This can be useful for more natural
              conversations, but may have a higher latency.

          voice: The voice the model uses to respond. Voice cannot be changed during the session
              once the model has responded with audio at least once. Current voice options are
              `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`,
              `shimmer`, and `verse`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/realtime/sessions",
            body=await async_maybe_transform(
                {
                    "input_audio_format": input_audio_format,
                    "input_audio_noise_reduction": input_audio_noise_reduction,
                    "input_audio_transcription": input_audio_transcription,
                    "instructions": instructions,
                    "max_response_output_tokens": max_response_output_tokens,
                    "modalities": modalities,
                    "model": model,
                    "output_audio_format": output_audio_format,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "turn_detection": turn_detection,
                    "voice": voice,
                },
                realtime_create_session_params.RealtimeCreateSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateSessionResponse,
        )

    async def create_transcription_session(
        self,
        *,
        include: List[str] | NotGiven = NOT_GIVEN,
        input_audio_format: Literal["pcm16", "g711_ulaw", "g711_alaw"] | NotGiven = NOT_GIVEN,
        input_audio_noise_reduction: realtime_create_transcription_session_params.InputAudioNoiseReduction
        | NotGiven = NOT_GIVEN,
        input_audio_transcription: realtime_create_transcription_session_params.InputAudioTranscription
        | NotGiven = NOT_GIVEN,
        modalities: List[Literal["text", "audio"]] | NotGiven = NOT_GIVEN,
        turn_detection: realtime_create_transcription_session_params.TurnDetection | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RealtimeCreateTranscriptionSessionResponse:
        """
        Create an ephemeral API token for use in client-side applications with the
        Realtime API specifically for realtime transcriptions. Can be configured with
        the same session parameters as the `transcription_session.update` client event.

        It responds with a session object, plus a `client_secret` key which contains a
        usable ephemeral API token that can be used to authenticate browser clients for
        the Realtime API.

        Args:
          include:
              The set of items to include in the transcription. Current available items are:

              - `item.input_audio_transcription.logprobs`

          input_audio_format: The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`. For
              `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate, single channel
              (mono), and little-endian byte order.

          input_audio_noise_reduction: Configuration for input audio noise reduction. This can be set to `null` to turn
              off. Noise reduction filters audio added to the input audio buffer before it is
              sent to VAD and the model. Filtering the audio can improve VAD and turn
              detection accuracy (reducing false positives) and model performance by improving
              perception of the input audio.

          input_audio_transcription: Configuration for input audio transcription. The client can optionally set the
              language and prompt for transcription, these offer additional guidance to the
              transcription service.

          modalities: The set of modalities the model can respond with. To disable audio, set this to
              ["text"].

          turn_detection: Configuration for turn detection, ether Server VAD or Semantic VAD. This can be
              set to `null` to turn off, in which case the client must manually trigger model
              response. Server VAD means that the model will detect the start and end of
              speech based on audio volume and respond at the end of user speech. Semantic VAD
              is more advanced and uses a turn detection model (in conjuction with VAD) to
              semantically estimate whether the user has finished speaking, then dynamically
              sets a timeout based on this probability. For example, if user audio trails off
              with "uhhm", the model will score a low probability of turn end and wait longer
              for the user to continue speaking. This can be useful for more natural
              conversations, but may have a higher latency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/realtime/transcription_sessions",
            body=await async_maybe_transform(
                {
                    "include": include,
                    "input_audio_format": input_audio_format,
                    "input_audio_noise_reduction": input_audio_noise_reduction,
                    "input_audio_transcription": input_audio_transcription,
                    "modalities": modalities,
                    "turn_detection": turn_detection,
                },
                realtime_create_transcription_session_params.RealtimeCreateTranscriptionSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateTranscriptionSessionResponse,
        )


class RealtimeResourceWithRawResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.create_session = to_raw_response_wrapper(
            realtime.create_session,
        )
        self.create_transcription_session = to_raw_response_wrapper(
            realtime.create_transcription_session,
        )


class AsyncRealtimeResourceWithRawResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.create_session = async_to_raw_response_wrapper(
            realtime.create_session,
        )
        self.create_transcription_session = async_to_raw_response_wrapper(
            realtime.create_transcription_session,
        )


class RealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.create_session = to_streamed_response_wrapper(
            realtime.create_session,
        )
        self.create_transcription_session = to_streamed_response_wrapper(
            realtime.create_transcription_session,
        )


class AsyncRealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.create_session = async_to_streamed_response_wrapper(
            realtime.create_session,
        )
        self.create_transcription_session = async_to_streamed_response_wrapper(
            realtime.create_transcription_session,
        )
