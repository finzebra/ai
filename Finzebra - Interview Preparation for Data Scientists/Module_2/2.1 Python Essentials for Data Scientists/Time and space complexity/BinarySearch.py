# O(log n) time complexity
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Initialize pointers
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
    return -1  # Return -1 if the target is not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 5))  # Output: 4 (index of 5)