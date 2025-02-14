def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example usage
a, b = 3, 8
for square in squares(a, b):
    print(square)
