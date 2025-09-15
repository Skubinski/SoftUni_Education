import math

def distance_to_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length1 = distance_to_center(x1, y1) + distance_to_center(x2, y2)
    length2 = distance_to_center(x3, y3) + distance_to_center(x4, y4)

    if length1 >= length2:
        return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"
    else:
        return f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})"

# Input: Coordinates of four points
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# Call the function and print the result
result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)
