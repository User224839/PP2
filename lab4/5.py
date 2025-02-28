import re

def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

# Example usage:
print(find_lowercase_with_underscore("hello_world example_text another_test"))
