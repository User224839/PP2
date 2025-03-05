from functools import reduce
import time
import math

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

numbers = [1, 2, 3, 4, 5]
print(f"Product of {numbers}: {multiply_list(numbers)}")  # Output: 120
