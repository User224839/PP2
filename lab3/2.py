import random
import itertools


def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(is_prime, numbers))

def string_permutations(s):
    return list(map("".join, itertools.permutations(s)))

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])