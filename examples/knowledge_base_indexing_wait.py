#!/usr/bin/env python3
"""
Example: Waiting for Knowledge Base Indexing Job Completion

This example demonstrates how to use the wait_for_completion() method
to automatically wait for a knowledge base indexing job to finish,
without needing to write manual polling loops.
"""

import os

from gradient import Gradient, IndexingJobError, IndexingJobTimeoutError


def main() -> None:
    # Initialize the Gradient client
    client = Gradient()

    # Example 1: Basic usage - wait for indexing job to complete
    print("Example 1: Basic usage")
    print("-" * 50)

    # Create an indexing job (replace with your actual knowledge base UUID)
    knowledge_base_uuid = os.getenv("KNOWLEDGE_BASE_UUID", "your-kb-uuid-here")

    print(f"Creating indexing job for knowledge base: {knowledge_base_uuid}")
    indexing_job = client.knowledge_bases.indexing_jobs.create(
        knowledge_base_uuid=knowledge_base_uuid,
    )

    job_uuid = indexing_job.job.uuid if indexing_job.job else None
    if not job_uuid:
        print("Error: Could not create indexing job")
        return

    print(f"Indexing job created with UUID: {job_uuid}")
    print("Waiting for indexing job to complete...")

    try:
        # Wait for the job to complete (polls every 5 seconds by default)
        completed_job = client.knowledge_bases.indexing_jobs.wait_for_completion(job_uuid)

        print("\n✅ Indexing job completed successfully!")
        if completed_job.job:
            print(f"Phase: {completed_job.job.phase}")
            print(f"Total datasources: {completed_job.job.total_datasources}")
            print(f"Completed datasources: {completed_job.job.completed_datasources}")

    except IndexingJobTimeoutError as e:
        print(f"\n⏱️ Timeout: {e}")
    except IndexingJobError as e:
        print(f"\n❌ Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


def example_with_custom_polling() -> None:
    """Example with custom polling interval and timeout"""
    print("\n\nExample 2: Custom polling interval and timeout")
    print("-" * 50)

    client = Gradient()
    knowledge_base_uuid = os.getenv("KNOWLEDGE_BASE_UUID", "your-kb-uuid-here")

    print(f"Creating indexing job for knowledge base: {knowledge_base_uuid}")
    indexing_job = client.knowledge_bases.indexing_jobs.create(
        knowledge_base_uuid=knowledge_base_uuid,
    )

    job_uuid = indexing_job.job.uuid if indexing_job.job else None
    if not job_uuid:
        print("Error: Could not create indexing job")
        return

    print(f"Indexing job created with UUID: {job_uuid}")
    print("Waiting for indexing job to complete (polling every 10 seconds, 5 minute timeout)...")

    try:
        # Wait with custom poll interval (10 seconds) and timeout (5 minutes = 300 seconds)
        completed_job = client.knowledge_bases.indexing_jobs.wait_for_completion(
            job_uuid,
            poll_interval=10,  # Poll every 10 seconds
            timeout=300,  # Timeout after 5 minutes
        )

        print("\n✅ Indexing job completed successfully!")
        if completed_job.job:
            print(f"Phase: {completed_job.job.phase}")

    except IndexingJobTimeoutError:
        print("\n⏱️ Job did not complete within 5 minutes")
        # You can still check the current status
        current_status = client.knowledge_bases.indexing_jobs.retrieve(job_uuid)
        if current_status.job:
            print(f"Current phase: {current_status.job.phase}")
            print(
                f"Completed datasources: {current_status.job.completed_datasources}/{current_status.job.total_datasources}"
            )
    except IndexingJobError as e:
        print(f"\n❌ Job failed: {e}")


def example_manual_polling() -> None:
    """Example of the old manual polling approach (for comparison)"""
    print("\n\nExample 3: Manual polling (old approach)")
    print("-" * 50)

    client = Gradient()
    knowledge_base_uuid = os.getenv("KNOWLEDGE_BASE_UUID", "your-kb-uuid-here")

    indexing_job = client.knowledge_bases.indexing_jobs.create(
        knowledge_base_uuid=knowledge_base_uuid,
    )

    job_uuid = indexing_job.job.uuid if indexing_job.job else None
    if not job_uuid:
        print("Error: Could not create indexing job")
        return

    print(f"Indexing job created with UUID: {job_uuid}")
    print("Manual polling (old approach)...")

    import time

    while True:
        indexing_job_status = client.knowledge_bases.indexing_jobs.retrieve(job_uuid)

        if indexing_job_status.job and indexing_job_status.job.phase:
            phase = indexing_job_status.job.phase
            print(f"Current phase: {phase}")

            if phase in ["BATCH_JOB_PHASE_UNKNOWN", "BATCH_JOB_PHASE_PENDING", "BATCH_JOB_PHASE_RUNNING"]:
                time.sleep(5)
                continue
            elif phase == "BATCH_JOB_PHASE_SUCCEEDED":
                print("✅ Job completed successfully!")
                break
            else:
                print(f"❌ Job ended with phase: {phase}")
                break


async def example_async() -> None:
    """Example using async/await"""
    print("\n\nExample 4: Async usage")
    print("-" * 50)

    from gradient import AsyncGradient

    client = AsyncGradient()
    knowledge_base_uuid = os.getenv("KNOWLEDGE_BASE_UUID", "your-kb-uuid-here")

    print(f"Creating indexing job for knowledge base: {knowledge_base_uuid}")
    indexing_job = await client.knowledge_bases.indexing_jobs.create(
        knowledge_base_uuid=knowledge_base_uuid,
    )

    job_uuid = indexing_job.job.uuid if indexing_job.job else None
    if not job_uuid:
        print("Error: Could not create indexing job")
        return

    print(f"Indexing job created with UUID: {job_uuid}")
    print("Waiting for indexing job to complete (async)...")

    try:
        completed_job = await client.knowledge_bases.indexing_jobs.wait_for_completion(
            job_uuid,
            poll_interval=5,
            timeout=600,  # 10 minute timeout
        )

        print("\n✅ Indexing job completed successfully!")
        if completed_job.job:
            print(f"Phase: {completed_job.job.phase}")

    except IndexingJobTimeoutError as e:
        print(f"\n⏱️ Timeout: {e}")
    except IndexingJobError as e:
        print(f"\n❌ Error: {e}")
    finally:
        await client.close()


if __name__ == "__main__":
    # Run the basic example
    main()

    # Uncomment to run other examples:
    # example_with_custom_polling()
    # example_manual_polling()

    # For async example, you would need to run:
    # import asyncio
    # asyncio.run(example_async())
