def binary (a, b):
    mask = a >> b
    shifted_mask = mask & 1
    return shifted_mask


number = int(input())
position = int(input())
print(binary(number, position))
