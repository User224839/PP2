def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# Input from console
n = int(input("Enter a number: "))
print(",".join(map(str, even_numbers(n))))