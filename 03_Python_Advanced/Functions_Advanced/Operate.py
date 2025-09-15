from functools import reduce

def operate(sign, *args):

    result = None
    if sign in "+-":
        result = 0
    elif sign in "*/":
        result = 1


    if sign == "+":
        result = reduce(lambda x, y: x + y, args)

    elif sign == "-":
        result = reduce(lambda x, y: x - y, args)

    elif sign == "*":
        result = reduce(lambda x, y: x * y, args)

    elif sign == "/":
        result = reduce(lambda x, y: x / y, args)

    return result

print(operate("+", 1, 2, 3))

print(operate("*", 3, 4))