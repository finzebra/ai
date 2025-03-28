# Slow recursive Fibonacci
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

# Optimized Fibonacci with memoization
def fibonacci_fast(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_fast(n - 1, memo) + fibonacci_fast(n - 2, memo)
    return memo[n]

# Example usage
print(fibonacci_slow(10))  # Output: 55 (slow)
print(fibonacci_fast(10))  # Output: 55 (fast)