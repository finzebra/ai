# List sorting example
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
ascending = sorted(numbers)  # Sort in ascending order
descending = sorted(numbers, reverse=True)  # Sort in descending order
print(ascending)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(descending)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]