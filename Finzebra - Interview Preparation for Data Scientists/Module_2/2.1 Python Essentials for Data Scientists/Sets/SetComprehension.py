# Create a set using set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}  # Create a set from the list
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}