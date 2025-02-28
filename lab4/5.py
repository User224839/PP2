import re

def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

# Example usage:
print(snake_to_camel("hello_world_test"))  # "HelloWorldTest"
