import re

def match_a_followed_by_2_to_3_b(string):
    return re.fullmatch(r'a{1}b{2,3}', string) is not None

# Example usage:
print(match_a_followed_by_2_to_3_b("abb"))  # True
