# O(n^2) time complexity
def nested_loop_example(lst):
    for i in range(len(lst)):  # Outer loop runs n times
        for j in range(len(lst)):  # Inner loop runs n times for each outer loop iteration
            print(lst[i], lst[j])  # Print pairs of elements

# Example usage
nested_loop_example([1, 2, 3])  # Output: (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)