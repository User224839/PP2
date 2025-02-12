import random
import itertools

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None
