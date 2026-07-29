# Migrate from Gradient SDK (Python) to pydo

> **This SDK (`gradient`) is deprecated and will be retired on August 15, 2026.**
> Please migrate to the unified DigitalOcean Python SDK: [`pydo`](https://github.com/digitalocean/pydo).
>
> Overview of official DigitalOcean libraries: https://docs.digitalocean.com/reference/libraries/

| From | To |
| --- | --- |
| `gradient` | `pydo` |

## 1. Replace the package

```sh
pip uninstall gradient
pip install pydo
# optional async extras
pip install "pydo[aio]"
```

## 2. Update credentials

Gradient used several auth modes on one client. Map each to pydo:

| Use case | Gradient (Python) | Env var (Gradient) | pydo |
| --- | --- | --- | --- |
| DigitalOcean API / GenAI control plane | `access_token=` | `DIGITALOCEAN_ACCESS_TOKEN` | `Client(token=...)` or `Client(api_key=...)` with a DigitalOcean PAT — prefer `DIGITALOCEAN_TOKEN` |
| Serverless inference | `model_access_key=` | `GRADIENT_MODEL_ACCESS_KEY` | `from pydo.inference import Client` → pass the same Model Access Key (or a **full-access** PAT) as `token` / `api_key` |
| Agent inference | `agent_access_key=` + `agent_endpoint=` | `GRADIENT_AGENT_ACCESS_KEY` + `GRADIENT_AGENT_ENDPOINT` | Pass the agent access key as `token` / `api_key` and set `agent_endpoint` on the client |

Notes:

- The Model Access Key **value** does not change — only the constructor / env name.
- Limited-scope PATs return **401** on inference; use a full-access PAT or a Model Access Key.
- Update `.env`, CI secrets, and runbooks accordingly.

## 3. Update client construction

### Serverless inference

**Before**

```python
from gradient import Gradient

client = Gradient(model_access_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"])
```

**After**

```python
from pydo.inference import Client

# Same Model Access Key value as GRADIENT_MODEL_ACCESS_KEY, or a full-access PAT
client = Client(api_key=os.environ["GRADIENT_MODEL_ACCESS_KEY"])
# equivalently:
# client = Client(token=os.environ["DIGITALOCEAN_TOKEN"])  # must be full-access
```

### Control-plane / GenAI management

**Before**

```python
from gradient import Gradient

client = Gradient(access_token=os.environ["DIGITALOCEAN_ACCESS_TOKEN"])
```

**After**

```python
from pydo import Client

# Same PAT value as DIGITALOCEAN_ACCESS_TOKEN; preferred env name is DIGITALOCEAN_TOKEN
client = Client(token=os.environ["DIGITALOCEAN_TOKEN"])
```

### Async Python

- **Before:** `from gradient import AsyncGradient`
- **After:** `from pydo.inference.aio import Client` or `from pydo.aio import Client` (prefer `async with`)

## 4. Update API call sites

Chat, streaming, images, and model listing keep a similar OpenAI-style shape. Only the import and client constructor change.

```python
# pydo inference
resp = client.chat.completions.create(
    model="llama3.3-70b-instruct",
    messages=[{"role": "user", "content": "Hello"}],
)
```

| Capability | Gradient | pydo |
| --- | --- | --- |
| Chat completions | `client.chat.completions.create` | same via `pydo.inference` |
| Streaming | `stream=True` | supported |
| Image generation | Gradient images APIs | `client.images.generate` |
| List models | Gradient models | `client.models.list` |
| Manage agents / GenAI | Gradient API client | top-level `pydo.Client` |

Rework error handling: Gradient Stainless `APIError` subclasses do not map 1:1 to pydo errors. Re-check retries and timeouts against the new client defaults.

## 5. Validate and remove Gradient

1. Confirm the app builds and runs with only `pydo`.
2. Smoke-test non-streaming chat, streaming chat, `models.list`, and images (if used).
3. Verify inference with a full-access PAT and, if applicable, a Model Access Key.
4. Remove `gradient` from lockfiles.
5. After cutover, remove unused Gradient env vars if you renamed them.
6. **Complete migration before August 15, 2026.**

## References

- https://docs.digitalocean.com/reference/libraries/
- https://github.com/digitalocean/pydo
- https://docs.digitalocean.com/reference/pydo/
- https://github.com/digitalocean/gradient-python (this repo — deprecated)
