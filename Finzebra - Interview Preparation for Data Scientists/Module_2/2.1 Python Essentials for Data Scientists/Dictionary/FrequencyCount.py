# Count frequencies of elements in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for fruit in fruits:
    if fruit in frequency:
        frequency[fruit] += 1  # Increment the count if the fruit is already in the dictionary
    else:
        frequency[fruit] = 1  # Add the fruit to the dictionary with a count of 1

print(frequency)