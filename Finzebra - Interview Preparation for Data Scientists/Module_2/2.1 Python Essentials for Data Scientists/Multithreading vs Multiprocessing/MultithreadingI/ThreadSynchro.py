import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # Acquire the lock
            counter += 1  # Safely increment the counter

# Create threads
threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")  # Output: 1000000