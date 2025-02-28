import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def replace_spaces_commas_dots():
    return re.sub(r'[ ,.]', ':', data)

print(replace_spaces_commas_dots())
