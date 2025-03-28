# Create a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Remove a key using del
del my_dict['city']

# Remove a key using pop()
age = my_dict.pop('age')

print(my_dict)  # Output: {'name': 'Alice'}
print(age)      # Output: 25