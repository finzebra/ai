# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: Elements in either set
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements in both sets
print(set1.intersection(set2))  # Output: {3, 4}

# Difference: Elements in set1 but not in set2
print(set1.difference(set2))  # Output: {1, 2}