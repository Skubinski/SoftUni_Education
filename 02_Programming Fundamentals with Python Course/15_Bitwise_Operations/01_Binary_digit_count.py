def binary_number (a, b):

    binary_digit = 0
    while a > 0:
        remainer = a % 2
        a = int(a / 2)
        if remainer == b:
            binary_digit += 1
    return binary_digit



number = int(input())
digit_0_or_1 = int(input())

print(binary_number(number, digit_0_or_1))