def find_multiplication_sign(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"
    elif (a < 0) ^ (b < 0) ^ (c < 0):
        return "negative"
    else:
        return "positive"

# Input: Three integers
a = int(input())
b = int(input())
c = int(input())

# Find and print the sign of the multiplication
result = find_multiplication_sign(a, b, c)
print(result)
