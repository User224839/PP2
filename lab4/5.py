import re

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

# Example usage:
print(split_at_uppercase("HelloWorldTest"))  # ['Hello', 'World', 'Test']
