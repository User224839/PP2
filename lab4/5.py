import re

def match_a_followed_by_b(string):
    return re.fullmatch(r'a*b*', string) is not None

# Example usage:
print(match_a_followed_by_b("abbb"))  # True
