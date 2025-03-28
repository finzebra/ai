# List copying example
original = [1, 2, 3]
shallow_copy = original[:]  # Create a shallow copy using slicing
deep_copy = original.copy()  # Create a shallow copy using the copy() method
print(shallow_copy)  # Output: [1, 2, 3]
print(deep_copy)  # Output: [1, 2, 3]