import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def camel_to_snake():
    return re.sub(r'(?<!^)(?=[A-Z])', '_', data).lower()

print(camel_to_snake())