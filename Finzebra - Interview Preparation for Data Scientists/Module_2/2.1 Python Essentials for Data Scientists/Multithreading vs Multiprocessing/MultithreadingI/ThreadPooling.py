from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(2)  # Simulate a task
    print(f"Finished task {name}")

# Create a thread pool
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]  # Submit tasks

# Wait for all tasks to complete
for future in futures:
    future.result()