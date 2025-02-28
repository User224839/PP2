import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def snake_to_camel():
    return re.sub(r'_(.)', lambda m: m.group(1).upper(), data)

print(snake_to_camel())