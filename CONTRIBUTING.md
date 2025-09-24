## Setting up the environment

### With Rye

We use [Rye](https://rye.astral.sh/) to manage dependencies because it will automatically provision a Python environment with the expected Python version. To set it up, run:

```sh
$ ./scripts/bootstrap
```

Or [install Rye manually](https://rye.astral.sh/guide/installation/) and run:

```sh
$ rye sync --all-features
```

You can then run scripts using `rye run python script.py` or by activating the virtual environment:

```sh
# Activate the virtual environment - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `rye run` prefix
$ python script.py
```

### Without Rye

Alternatively if you don't want to install `Rye`, you can stick with the standard `pip` setup by ensuring you have the Python version specified in `.python-version`, create a virtual environment however you desire and then install dependencies using this command:

```sh
$ pip install -r requirements-dev.lock
```

## Modifying/Adding code

Most of the SDK is generated code. Modifications to code will be persisted between generations, but may
result in merge conflicts between manual patches and changes from the generator. The generator will never
modify the contents of the `src/gradient/lib/` and `examples/` directories.

## Adding and running examples

All files in the `examples/` directory are not modified by the generator and can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S rye run python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/digitalocean/gradient-python.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ rye build
# or
$ python -m build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

Most tests require you to [set up a mock server](https://github.com/stoplightio/prism) against the OpenAPI spec to run the tests.

```sh
# you will need npm installed
$ npx prism mock path/to/your/openapi.yml
```

```sh
$ ./scripts/test
```

## Smoke tests & environment variables

The repository includes a small set of live "smoke" tests (see the `smoke` pytest marker) that exercise real Gradient API endpoints. These are excluded from the default test run and only executed when you explicitly target them (`pytest -m smoke`) or in CI via the dedicated `smoke` job.

Required environment variables for smoke tests (all must be set):

| Variable | Purpose |
|----------|---------|
| `DIGITALOCEAN_ACCESS_TOKEN` | Access token for core DigitalOcean Gradient API operations (e.g. listing agents). |
| `GRADIENT_MODEL_ACCESS_KEY` | Key used for serverless inference (chat completions, etc.). |
| `GRADIENT_AGENT_ACCESS_KEY` | Key used for agent-scoped inference requests. |
| `GRADIENT_AGENT_ENDPOINT` | Fully-qualified HTTPS endpoint for your deployed agent (e.g. `https://my-agent.agents.do-ai.run`). |

Optional override:

| Variable | Purpose |
|----------|---------|
| `GRADIENT_INFERENCE_ENDPOINT` | Override default inference endpoint (`https://inference.do-ai.run`). |

Create a local `.env` file (never commit real secrets). A template is provided at `.env.example`.

Key design notes:
* Sync & async suites each have a single central test that asserts environment presence and client auto-loaded properties.
* Other smoke tests intentionally avoid repeating environment / property assertions to keep noise low.
* Add new credentials by updating the `REQUIRED_ENV_VARS` tuple in both smoke test files and documenting them here and in the README.

Run smoke tests locally:

```bash
./scripts/smoke            # convenience wrapper
pytest -m smoke -q         # direct invocation
```

Do NOT run smoke tests against production credentials unless you understand the API calls performed—they make real network requests.

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) and
[black](https://github.com/psf/black) to format the code in the repository.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

Changes made to this repository via the automated release PR pipeline should publish to PyPI automatically. If
the changes aren't made through the automated pipeline, you may want to make releases manually.

### Publish with a GitHub workflow

You can release to package managers by using [the `Publish PyPI` GitHub action](https://www.github.com/digitalocean/gradient-python/actions/workflows/publish-pypi.yml). This requires a setup organization or repository secret to be set up.

### Publish manually

If you need to manually release a package, you can run the `bin/publish-pypi` script with a `PYPI_TOKEN` set on
the environment.
