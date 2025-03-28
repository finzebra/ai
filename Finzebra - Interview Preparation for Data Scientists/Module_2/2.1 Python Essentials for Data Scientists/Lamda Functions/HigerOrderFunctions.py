# Higher-order function with lambda
def apply_function(func, value):
    return func(value)

# Use a lambda function as an argument
result = apply_function(lambda x: x * 2, 5)  # Double the value
print(result)  # Output: 10