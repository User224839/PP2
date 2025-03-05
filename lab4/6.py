from functools import reduce
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return f"Square root of {number} after {delay_ms} milliseconds is {math.sqrt(number)}"

number = 25100
delay = 2123
print(delayed_sqrt(number, delay)) 