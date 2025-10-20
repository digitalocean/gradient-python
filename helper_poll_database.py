import time

def poll_database_creation(get_status_func, database_id, interval=5, timeout=300):
    """
    Polls for the completion of a knowledge-based database creation.

    Parameters:
    - get_status_func: a function that takes database_id and returns its status as string
    - database_id: the ID of the database to poll
    - interval: seconds between each poll (default 5s)
    - timeout: maximum seconds to wait (default 300s)

    Returns:
    - status: final status of the database creation ('completed', 'failed', etc.)
    """
    start_time = time.time()

    while True:
        status = get_status_func(database_id)
        if status.lower() == 'completed':
            print(f"Database {database_id} creation completed!")
            return status
        elif status.lower() == 'failed':
            print(f"Database {database_id} creation failed.")
            return status

        if time.time() - start_time > timeout:
            print(f"Timeout reached for database {database_id}.")
            return 'timeout'

        print(f"Database {database_id} status: {status}. Polling again in {interval}s...")
        time.sleep(interval)

# Test example
if __name__ == "__main__":
    import random

    def dummy_get_status(database_id):
        # Simulate database creation status
        return random.choice(['pending', 'pending', 'completed'])

    poll_database_creation(dummy_get_status, database_id="DB123", interval=1, timeout=10)
