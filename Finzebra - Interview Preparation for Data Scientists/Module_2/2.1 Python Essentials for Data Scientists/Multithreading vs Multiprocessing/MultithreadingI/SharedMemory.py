import multiprocessing

def worker(shared_value):
    shared_value.value += 1  # Modify the shared value

if __name__ == "__main__":
    shared_value = multiprocessing.Value('i', 0)  # Shared integer
    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=worker, args=(shared_value,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final shared value: {shared_value.value}")  # Output: 10