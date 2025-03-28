# O(n) time complexity
def sum_of_list(lst):
    total = 0  # Initialize total to 0
    for num in lst:  # Loop through each element in the list
        total += num  # Add the current element to the total
    return total  # Return the sum

# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_of_list(numbers))  # Output: 15