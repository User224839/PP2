def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print("*" * num)