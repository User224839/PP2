import re

def read_file():
    with open('row.txt', 'r', encoding='utf-8') as file:
        return file.read()

data = read_file()

def match_a_followed_by_anything_ending_in_b():
    return re.findall(r'a.*b', data)

print(match_a_followed_by_anything_ending_in_b())