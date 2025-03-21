# Filtering with lambda
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filter even numbers
print(even_numbers)  # Output: [2, 4, 6]