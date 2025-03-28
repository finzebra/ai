# Create a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Iterate over keys
for key in my_dict:
    print(key)  # Output: name, age, city

# Iterate over values
for value in my_dict.values():
    print(value)  # Output: Alice, 25, New York

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 25, city: New York