import math

def regular_polygon_area(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

# Example usage
n = 4  # Number of sides
side_length = 25
area = regular_polygon_area(n, side_length)

print(f"Input number of sides: {n}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.2f}")
