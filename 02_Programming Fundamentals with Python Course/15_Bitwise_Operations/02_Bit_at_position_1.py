def binary (a):
    mask = a >> 1
    shifted_mask = mask & 1
    return shifted_mask


number = int(input())
print(binary(number))
