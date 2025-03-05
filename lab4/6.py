from functools import reduce
import time
import math

def all_true(tpl):
    return all(tpl)

tpl1 = (True, True, True)
tpl2 = (True, False, True)

print(f"Are all elements in {tpl1} true? {all_true(tpl1)}")  
print(f"Are all elements in {tpl2} true? {all_true(tpl2)}")  