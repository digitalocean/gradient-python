import time

def poll_agent_deployment(get_status_func, agent_id, interval=5, timeout=300):
    """
    Polls for the readiness of an agent deployment.

    Parameters:
    - get_status_func: function that takes agent_id and returns its status as string
    - agent_id: the ID of the agent to poll
    - interval: seconds between each poll (default 5s)
    - timeout: maximum seconds to wait (default 300s)

    Returns:
    - status: final status of the agent deployment ('ready', 'failed', etc.)
    """
    start_time = time.time()

    while True:
        status = get_status_func(agent_id)
        if status.lower() == 'ready':
            print(f"Agent {agent_id} is ready!")
            return status
        elif status.lower() == 'failed':
            print(f"Agent {agent_id} deployment failed.")
            return status

        if time.time() - start_time > timeout:
            print(f"Timeout reached for agent {agent_id}.")
            return 'timeout'

        print(f"Agent {agent_id} status: {status}. Polling again in {interval}s...")
        time.sleep(interval)

if __name__ == "__main__":
    import random

    def dummy_get_status(agent_id):
        return random.choice(['pending', 'pending', 'ready'])

    poll_agent_deployment(dummy_get_status, agent_id="AGT123", interval=1, timeout=10)
