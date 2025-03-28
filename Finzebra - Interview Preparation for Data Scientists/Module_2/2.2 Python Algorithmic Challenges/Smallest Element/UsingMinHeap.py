import heapq

# Function to find the k-th smallest element using a min-heap
def find_kth_smallest_min_heap(arr, k):
    heapq.heapify(arr)  # Convert the array into a min-heap
    for _ in range(k - 1):
        heapq.heappop(arr)  # Remove the smallest elements
    return heapq.heappop(arr)  # Return the k-th smallest element

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(find_kth_smallest_min_heap(arr, k))  # Output: 7