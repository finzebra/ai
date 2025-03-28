# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]  # Compare the string to its reverse

# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False