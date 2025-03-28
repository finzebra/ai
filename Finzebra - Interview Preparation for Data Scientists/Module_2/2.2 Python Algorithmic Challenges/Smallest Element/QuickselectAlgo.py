# Function to find the k-th smallest element using Quickselect
def find_kth_smallest_quickselect(arr, k):
    def quickselect(left, right):
        pivot_index = partition(left, right)
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index < k - 1:
            return quickselect(pivot_index + 1, right)
        else:
            return quickselect(left, pivot_index - 1)

    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    return quickselect(0, len(arr) - 1)

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(find_kth_smallest_quickselect(arr, k))  # Output: 7