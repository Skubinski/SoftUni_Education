def add_and_subtract(a, b, c):

    def sum (a, b):
        return a + b
    def sub (c):
        return sum(a, b) - c

    return sub(c)
a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))
