import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def find_lowercase_with_underscore():
    return re.findall(r'\b[a-z]+_[a-z]+\b', data)

print(find_lowercase_with_underscore())
