# Flatten a 2D list using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]  # Flatten the matrix
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]