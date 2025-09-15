def between_characters (a, b):
    a = ord(a)
    b = ord(b)
    for i in range(a, b-1):
        current_number = i + 1
        if i == 0:
            continue
        print(chr(current_number), end=" ")

a = input()
b = input()
between_characters(a, b)