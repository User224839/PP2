import re

def insert_spaces_in_camel_case(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

# Example usage:
print(insert_spaces_in_camel_case("HelloWorldTest"))  # "Hello World Test"
