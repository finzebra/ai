# Sorting with lambda
data = [(1, 3), (4, 1), (2, 2)]
sorted_data = sorted(data, key=lambda x: x[1])  # Sort by the second element
print(sorted_data)  # Output: [(4, 1), (2, 2), (1, 3)]