import re

def replace_spaces_commas_dots(string):
    return re.sub(r'[ ,.]', ':', string)

# Example usage:
print(replace_spaces_commas_dots("Hello, world. Test string"))  # "Hello:world:Test:string"
