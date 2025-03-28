# Removing whitespace and special characters
text = "  Hello, World!  "

# Remove leading and trailing whitespace
cleaned_text = text.strip()
print(cleaned_text)  # Output: Hello, World!

# Remove special characters
import re
text_with_special_chars = "Hello, @World! #2023"
cleaned_text = re.sub(r'[^\w\s]', '', text_with_special_chars)  # Remove non-alphanumeric characters
print(cleaned_text)  # Output: Hello World 2023