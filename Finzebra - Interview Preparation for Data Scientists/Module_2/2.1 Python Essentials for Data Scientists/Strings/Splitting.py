# Splitting and joining strings
text = "Hello, World! How are you?"

# Split the string into words
words = text.split()  # Split by spaces
print(words)  # Output: ['Hello,', 'World!', 'How', 'are', 'you?']

# Join the words back into a string
new_text = " ".join(words)  # Join with spaces
print(new_text)  # Output: Hello, World! How are you?