import threading
import time

def download_file(file_name):
    print(f"Downloading {file_name}...")
    time.sleep(2)  # Simulate a download delay
    print(f"Finished downloading {file_name}")

# Create threads for each file
threads = []
files = ["file1.txt", "file2.txt", "file3.txt"]
for file in files:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All files downloaded.")
