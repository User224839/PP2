import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def insert_spaces_in_camel_case():
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', data)

print(insert_spaces_in_camel_case())