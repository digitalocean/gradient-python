![Header image for the DigitalOcean Gradient AI Agentic Cloud](https://doimages.nyc3.cdn.digitaloceanspaces.com/do_gradient_ai_agentic_cloud.svg)

# Gradient Python API library

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/gradient.svg?label=pypi%20(stable))](https://pypi.org/project/gradient/)
[![Docs](https://img.shields.io/badge/Docs-8A2BE2)](https://gradientai.digitalocean.com/getting-started/overview/)

The Gradient Python library provides convenient access to the Gradient REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated with [Stainless](https://www.stainless.com/).

## Documentation

The getting started guide can be found on [gradient-sdk.digitalocean.com](https://gradient-sdk.digitalocean.com/getting-started/overview).
The REST API documentation can be found on [developers.digitalocean.com](https://developers.digitalocean.com/documentation/v2/).
The full API of this library can be found in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install gradient
```

## Usage

The Gradient SDK provides clients for:
* DigitalOcean API
* Gradient Serverless Inference
* Gradient Agent Inference

The full API of this library can be found in [api.md](api.md).

```python
import os
from gradient import Gradient

client = Gradient(
    access_token=os.environ.get(
        "DIGITALOCEAN_ACCESS_TOKEN"
    ),  # This is the default and can be omitted
)
inference_client = Gradient(
    model_access_key=os.environ.get(
        "GRADIENT_MODEL_ACCESS_KEY"
    ),  # This is the default and can be omitted
)
agent_client = Gradient(
    agent_access_key=os.environ.get(
        "GRADIENT_AGENT_ACCESS_KEY"
    ),  # This is the default and can be omitted
    agent_endpoint="https://my-agent.agents.do-ai.run",
)

## API
api_response = api_client.agents.list()
print("--- API")
if api_response.agents:
    print(api_response.agents[0].name)


## Serverless Inference
inference_response = inference_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="llama3.3-70b-instruct",
)

print("--- Serverless Inference")
print(inference_response.choices[0].message.content)

## Agent Inference
agent_response = agent_client.agents.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of Portugal?",
        }
    ],
    model="llama3.3-70b-instruct",
)

print("--- Agent Inference")
print(agent_response.choices[0].message.content)
```

While you can provide an `access_token`, `model_access_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `DIGITALOCEAN_ACCESS_TOKEN="My Access Token"`, `GRADIENT_MODEL_ACCESS_KEY="My Model Access Key"` to your `.env` file
so that your keys are not stored in source control.

## Async usage

Simply import `AsyncGradient` instead of `Gradient` and use `await` with each API call:

```python
import os
import asyncio
from gradient import AsyncGradient

client = AsyncGradient()


async def main() -> None:
    completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
            }
        ],
        model="llama3.3-70b-instruct",
    )
    print(completion.choices)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install gradient[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from gradient import DefaultAioHttpClient
from gradient import AsyncGradient


async def main() -> None:
    async with AsyncGradient(
        model_access_key=os.environ.get(
            "GRADIENT_MODEL_ACCESS_KEY"
        ),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "What is the capital of France?",
                }
            ],
            model="llama3.3-70b-instruct",
        )
        print(completion.choices)


asyncio.run(main())
```

## Streaming responses

We provide support for streaming responses using Server Side Events (SSE).

```python
from gradient import Gradient

client = Gradient()

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="llama3.3-70b-instruct",
    stream=True,
)
for completion in stream:
    print(completion.choices)
```

The async client uses the exact same interface.

```python
from gradient import AsyncGradient

client = AsyncGradient()

stream = await client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="llama3.3-70b-instruct",
    stream=True,
)
async for completion in stream:
    print(completion.choices)
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from gradient import Gradient

client = Gradient()

completion = client.chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "system",
        }
    ],
    model="llama3-8b-instruct",
    stream_options={},
)
print(completion.stream_options)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `gradient.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `gradient.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `gradient.APIError`.

```python
import gradient
from gradient import Gradient

client = Gradient()

try:
    client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
            }
        ],
        model="llama3.3-70b-instruct",
    )
except gradient.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except gradient.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except gradient.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from gradient import Gradient

# Configure the default for all requests:
client = Gradient(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="llama3.3-70b-instruct",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from gradient import Gradient

# Configure the default for all requests:
client = Gradient(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Gradient(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="llama3.3-70b-instruct",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `GRADIENT_LOG` to `info`.

```shell
$ export GRADIENT_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from gradient import Gradient

client = Gradient()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "What is the capital of France?",
    }],
    model="llama3.3-70b-instruct",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion.choices)
```

These methods return an [`APIResponse`](https://github.com/digitalocean/gradient-python/tree/main/src/gradient/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/digitalocean/gradient-python/tree/main/src/gradient/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="llama3.3-70b-instruct",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from gradient import Gradient, DefaultHttpxClient

client = Gradient(
    # Or use the `GRADIENT_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from gradient import Gradient

with Gradient() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/digitalocean/gradient-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import gradient
print(gradient.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).

## Smoke tests

The repository includes a small set of "smoke" tests that exercise live Gradient API / Inference / Agent endpoints to catch integration regressions early. These tests are intentionally excluded from the standard test run (they are marked with the `smoke` pytest marker) and only run in CI via the dedicated `smoke` job, or when you explicitly target them locally.

### Required environment variables

All of the following environment variables must be set for the smoke tests (both sync & async) to run. If any are missing the smoke tests will fail fast:

| Variable | Purpose |
|----------|---------|
| `DIGITALOCEAN_ACCESS_TOKEN` | Access token for core DigitalOcean Gradient API operations (e.g. listing agents). |
| `GRADIENT_MODEL_ACCESS_KEY` | Key used for serverless inference (chat completions, etc.). |
| `GRADIENT_AGENT_ACCESS_KEY` | Key used for agent-scoped inference requests. |
| `GRADIENT_AGENT_ENDPOINT` | Fully-qualified HTTPS endpoint for your deployed agent (e.g. `https://my-agent.agents.do-ai.run`). |

> Optional override: `GRADIENT_INFERENCE_ENDPOINT` can be provided to point inference to a non-default endpoint (defaults to `https://inference.do-ai.run`).

### Running smoke tests locally

1. Export the required environment variables (or place them in a `.env` file and use a tool like `direnv` or `python-dotenv`).
2. Run only the smoke tests:

```bash
rye run pytest -m smoke -q
```

To include them alongside the regular suite:

```bash
./scripts/test -m smoke
```

Convenience wrapper (auto-loads a local `.env` if present):

```bash
./scripts/smoke
```

See `.env.example` for a template of required variables you can copy into a `.env` file (do not commit secrets).

### Async variants

Each smoke test has an async counterpart in `tests/test_smoke_sdk_async.py`. Both sets are covered automatically by the `-m smoke` selection.

### CI behavior

The default `test` job excludes smoke tests (`-m 'not smoke'`). A separate `smoke` job runs on pushes to the main repository with the required secrets injected. This keeps contributors from inadvertently hitting live services while still providing integration coverage in controlled environments.

### Adding new smoke tests

1. Add a new test function to `tests/test_smoke_sdk.py` and/or `tests/test_smoke_sdk_async.py`.
2. Mark it with `@pytest.mark.smoke`.
3. Avoid duplicating environment or client property assertions—those live in the central environment/client state test (sync & async).
4. Keep assertions minimal—verify only surface contract / structure; deeper behavior belongs in unit tests with mocks.

If a new credential is required, update this README section, the `REQUIRED_ENV_VARS` list in both smoke test files, and the CI workflow's `smoke` job environment.


## License

Licensed under the Apache License 2.0. See [LICENSE](./LICENSE)
