import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def match_a_followed_by_2_to_3_b():
    return re.findall(r'a{1}b{2,3}', data)

print(match_a_followed_by_2_to_3_b())
