"""
Example: Wait for Agent Deployment to Complete

This example demonstrates how to use the wait_until_ready() method to wait for
an agent to finish deploying before using it.
"""

from gradient import Gradient, AgentDeploymentError, AgentDeploymentTimeoutError

# Initialize the Gradient client
client = Gradient()

# Create a new agent
agent_response = client.agents.create(
    name="My Agent",
    instruction="You are a helpful assistant",
    model_uuid="<your-model-uuid>",
    region="nyc1",
)

agent_id = agent_response.agent.uuid if agent_response.agent else None

if agent_id:
    print(f"Agent created with ID: {agent_id}")
    print("Waiting for agent to be ready...")

    try:
        # Wait for the agent to be deployed and ready
        # This will poll the agent status every 5 seconds (default)
        # and wait up to 5 minutes (default timeout=300 seconds)
        ready_agent = client.agents.wait_until_ready(
            agent_id,
            poll_interval=5.0,  # Check every 5 seconds
            timeout=300.0,  # Wait up to 5 minutes
        )

        if ready_agent.agent and ready_agent.agent.deployment:
            print(f"Agent is ready! Status: {ready_agent.agent.deployment.status}")
            print(f"Agent URL: {ready_agent.agent.url}")

        # Now you can use the agent
        # ...

    except AgentDeploymentError as e:
        print(f"Agent deployment failed: {e}")
        print(f"Failed status: {e.status}")

    except AgentDeploymentTimeoutError as e:
        print(f"Agent deployment timed out: {e}")
        print(f"Agent ID: {e.agent_id}")

    except Exception as e:
        print(f"Unexpected error: {e}")


# Async example
from gradient import AsyncGradient


async def main() -> None:
    async_client = AsyncGradient()

    # Create a new agent
    agent_response = await async_client.agents.create(
        name="My Async Agent",
        instruction="You are a helpful assistant",
        model_uuid="<your-model-uuid>",
        region="nyc1",
    )

    agent_id = agent_response.agent.uuid if agent_response.agent else None

    if agent_id:
        print(f"Agent created with ID: {agent_id}")
        print("Waiting for agent to be ready...")

        try:
            # Wait for the agent to be deployed and ready (async)
            ready_agent = await async_client.agents.wait_until_ready(
                agent_id,
                poll_interval=5.0,
                timeout=300.0,
            )

            if ready_agent.agent and ready_agent.agent.deployment:
                print(f"Agent is ready! Status: {ready_agent.agent.deployment.status}")
                print(f"Agent URL: {ready_agent.agent.url}")

        except AgentDeploymentError as e:
            print(f"Agent deployment failed: {e}")
            print(f"Failed status: {e.status}")

        except AgentDeploymentTimeoutError as e:
            print(f"Agent deployment timed out: {e}")
            print(f"Agent ID: {e.agent_id}")


# Uncomment to run async example
# asyncio.run(main())
