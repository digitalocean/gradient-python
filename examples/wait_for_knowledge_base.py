"""
Example demonstrating how to use the wait_for_database helper function.

This example shows how to:
1. Create a knowledge base
2. Wait for its database to be ready
3. Handle errors and timeouts appropriately
"""

import os

from gradient import Gradient
from gradient.resources.knowledge_bases import KnowledgeBaseTimeoutError, KnowledgeBaseDatabaseError


def main() -> None:
    """Create a knowledge base and wait for its database to be ready."""
    # Initialize the Gradient client
    # Note: DIGITALOCEAN_ACCESS_TOKEN must be set in your environment
    client = Gradient(
        access_token=os.environ.get("DIGITALOCEAN_ACCESS_TOKEN"),
    )

    # Create a knowledge base
    # Replace these values with your actual configuration
    kb_response = client.knowledge_bases.create(
        name="My Knowledge Base",
        region="nyc1",  # Choose your preferred region
        embedding_model_uuid="your-embedding-model-uuid",  # Use your embedding model UUID
    )

    if not kb_response.knowledge_base or not kb_response.knowledge_base.uuid:
        print("Failed to create knowledge base")
        return

    kb_uuid = kb_response.knowledge_base.uuid
    print(f"Created knowledge base: {kb_uuid}")

    try:
        # Wait for the database to be ready
        # Default: 10 minute timeout, 5 second poll interval
        print("Waiting for database to be ready...")
        result = client.knowledge_bases.wait_for_database(kb_uuid)
        print(f"Database status: {result.database_status}")  # "ONLINE"
        print("Knowledge base is ready!")

        # Alternative: Custom timeout and poll interval
        # result = client.knowledge_bases.wait_for_database(
        #     kb_uuid,
        #     timeout=900.0,       # 15 minutes
        #     poll_interval=10.0   # Check every 10 seconds
        # )

    except KnowledgeBaseDatabaseError as e:
        # Database entered a failed state (DECOMMISSIONED or UNHEALTHY)
        print(f"Database failed: {e}")

    except KnowledgeBaseTimeoutError as e:
        # Database did not become ready within the timeout period
        print(f"Timeout: {e}")


if __name__ == "__main__":
    main()
