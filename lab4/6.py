from functools import reduce
import time
import math

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"Uppercase": upper, "Lowercase": lower}

text = "Hello World!"
print(f"Upper and lower case count in '{text}': {count_case(text)}") 