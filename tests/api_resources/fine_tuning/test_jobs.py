# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from digitalocean_genai_sdk import DigitaloceanGenaiSDK, AsyncDigitaloceanGenaiSDK
from digitalocean_genai_sdk.types.fine_tuning import (
    FineTuningJob,
    JobListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: DigitaloceanGenaiSDK) -> None:
        job = client.fine_tuning.jobs.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        job = client.fine_tuning.jobs.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
            hyperparameters={
                "batch_size": "auto",
                "learning_rate_multiplier": "auto",
                "n_epochs": "auto",
            },
            integrations=[
                {
                    "type": "wandb",
                    "wandb": {
                        "project": "my-wandb-project",
                        "entity": "entity",
                        "name": "name",
                        "tags": ["custom-tag"],
                    },
                }
            ],
            metadata={"foo": "string"},
            method={
                "dpo": {
                    "hyperparameters": {
                        "batch_size": "auto",
                        "beta": "auto",
                        "learning_rate_multiplier": "auto",
                        "n_epochs": "auto",
                    }
                },
                "supervised": {
                    "hyperparameters": {
                        "batch_size": "auto",
                        "learning_rate_multiplier": "auto",
                        "n_epochs": "auto",
                    }
                },
                "type": "supervised",
            },
            seed=42,
            suffix="x",
            validation_file="file-abc123",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.jobs.with_raw_response.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.jobs.with_streaming_response.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(FineTuningJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        job = client.fine_tuning.jobs.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.jobs.with_raw_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.jobs.with_streaming_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(FineTuningJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tuning_job_id` but received ''"):
            client.fine_tuning.jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: DigitaloceanGenaiSDK) -> None:
        job = client.fine_tuning.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: DigitaloceanGenaiSDK) -> None:
        job = client.fine_tuning.jobs.list(
            after="after",
            limit=0,
            metadata={"foo": "string"},
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        job = client.fine_tuning.jobs.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        response = client.fine_tuning.jobs.with_raw_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        with client.fine_tuning.jobs.with_streaming_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(FineTuningJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel(self, client: DigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tuning_job_id` but received ''"):
            client.fine_tuning.jobs.with_raw_response.cancel(
                "",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        job = await async_client.fine_tuning.jobs.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        job = await async_client.fine_tuning.jobs.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
            hyperparameters={
                "batch_size": "auto",
                "learning_rate_multiplier": "auto",
                "n_epochs": "auto",
            },
            integrations=[
                {
                    "type": "wandb",
                    "wandb": {
                        "project": "my-wandb-project",
                        "entity": "entity",
                        "name": "name",
                        "tags": ["custom-tag"],
                    },
                }
            ],
            metadata={"foo": "string"},
            method={
                "dpo": {
                    "hyperparameters": {
                        "batch_size": "auto",
                        "beta": "auto",
                        "learning_rate_multiplier": "auto",
                        "n_epochs": "auto",
                    }
                },
                "supervised": {
                    "hyperparameters": {
                        "batch_size": "auto",
                        "learning_rate_multiplier": "auto",
                        "n_epochs": "auto",
                    }
                },
                "type": "supervised",
            },
            seed=42,
            suffix="x",
            validation_file="file-abc123",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.jobs.with_raw_response.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.jobs.with_streaming_response.create(
            model="gpt-4o-mini",
            training_file="file-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(FineTuningJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        job = await async_client.fine_tuning.jobs.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.jobs.with_raw_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.jobs.with_streaming_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(FineTuningJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tuning_job_id` but received ''"):
            await async_client.fine_tuning.jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        job = await async_client.fine_tuning.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        job = await async_client.fine_tuning.jobs.list(
            after="after",
            limit=0,
            metadata={"foo": "string"},
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        job = await async_client.fine_tuning.jobs.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        response = await async_client.fine_tuning.jobs.with_raw_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(FineTuningJob, job, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        async with async_client.fine_tuning.jobs.with_streaming_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(FineTuningJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncDigitaloceanGenaiSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tuning_job_id` but received ''"):
            await async_client.fine_tuning.jobs.with_raw_response.cancel(
                "",
            )
