def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Example usage
n = 10
for num in countdown(n):
    print(num, end=" ")