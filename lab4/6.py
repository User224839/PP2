from functools import reduce
import time
import math

def is_palindrome(s):
    return s == s[::-1]

word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}") 

word2 = "hello"
print(f"Is '{word2}' a palindrome? {is_palindrome(word2)}") 