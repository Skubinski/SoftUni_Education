def invert_bits_at_position(number, p):

    mask = 7 << p


    result = number ^ mask

    return result


input_number = int(input())
position = int(input())

if 0 <= position <= 29:
    inverted_number = invert_bits_at_position(input_number, position)
    print(inverted_number)

