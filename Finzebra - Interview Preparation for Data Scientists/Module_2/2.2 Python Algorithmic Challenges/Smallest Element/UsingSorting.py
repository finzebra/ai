# Function to find the k-th smallest element using sorting
def find_kth_smallest_sorting(arr, k):
    arr.sort()  # Sort the array
    return arr[k - 1]  # Return the k-th smallest element (0-based index)

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(find_kth_smallest_sorting(arr, k))  # Output: 7