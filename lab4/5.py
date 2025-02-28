import re

def find_uppercase_followed_by_lowercase(string):
    return re.findall(r'[A-Z][a-z]+', string)

# Example usage:
print(find_uppercase_followed_by_lowercase("Hello World Test String"))
