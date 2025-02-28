import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def split_at_uppercase():
    return re.split(r'(?=[A-Z])', data)

print(split_at_uppercase())