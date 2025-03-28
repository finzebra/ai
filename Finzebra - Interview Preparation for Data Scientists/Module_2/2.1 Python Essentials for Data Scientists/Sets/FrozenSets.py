# Create a frozen set
my_frozen_set = frozenset([1, 2, 3, 4])

# Use a frozen set as a dictionary key
my_dict = {my_frozen_set: 'frozen set'}
print(my_dict)  # Output: {frozenset({1, 2, 3, 4}): 'frozen set'}