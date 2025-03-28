# O(2^n) time complexity
def fibonacci(n):
    if n <= 1:
        return n  # Base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example usage
print(fibonacci(5))  # Output: 5