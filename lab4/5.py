import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def find_uppercase_followed_by_lowercase():
    return re.findall(r'[A-Z][a-z]+', data)

print(find_uppercase_followed_by_lowercase())
