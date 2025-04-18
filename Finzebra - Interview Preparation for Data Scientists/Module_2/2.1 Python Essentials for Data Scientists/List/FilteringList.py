# Filter even numbers using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]  # Filter even numbers
print(even_numbers)  # Output: [2, 4, 6, 8, 10]