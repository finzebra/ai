from functools import reduce

# Reduce with lambda
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  # Calculate the product
print(product)  # Output: 24