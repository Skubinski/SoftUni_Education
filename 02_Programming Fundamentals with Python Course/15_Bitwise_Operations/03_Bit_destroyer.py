def destroyer (a, b):
    mask = 1 << b
    reversed_mask = ~mask
    result = a & reversed_mask
    return result



number = int(input())
position = int(input())
print(destroyer(number, position))