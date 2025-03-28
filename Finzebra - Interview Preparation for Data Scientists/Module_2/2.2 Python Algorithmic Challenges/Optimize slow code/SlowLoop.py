# Slow version
def sum_of_squares_slow(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

# Optimized version using list comprehension and sum()
def sum_of_squares_fast(numbers):
    return sum(num ** 2 for num in numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_of_squares_slow(numbers))  # Output: 55
print(sum_of_squares_fast(numbers))  # Output: 55