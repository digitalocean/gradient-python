import time

def poll_indexing_completion(get_status_func, index_id, interval=5, timeout=300):
    """
    Polls for the completion of a knowledge-based indexing process.

    Parameters:
    - get_status_func: function that takes index_id and returns its status as string
    - index_id: the ID of the index to poll
    - interval: seconds between each poll (default 5s)
    - timeout: maximum seconds to wait (default 300s)

    Returns:
    - status: final status of the indexing process ('completed', 'failed', etc.)
    """
    start_time = time.time()

    while True:
        status = get_status_func(index_id)
        if status.lower() == 'completed':
            print(f"Index {index_id} completed!")
            return status
        elif status.lower() == 'failed':
            print(f"Index {index_id} failed.")
            return status

        if time.time() - start_time > timeout:
            print(f"Timeout reached for index {index_id}.")
            return 'timeout'

        print(f"Index {index_id} status: {status}. Polling again in {interval}s...")
        time.sleep(interval)

if __name__ == "__main__":
    import random

    def dummy_get_status(index_id):
        return random.choice(['pending', 'pending', 'completed'])

    poll_indexing_completion(dummy_get_status, index_id="IDX123", interval=1, timeout=10)
