# Remove duplicates from a list using a set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))  # Convert the list to a set and back to a list
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]