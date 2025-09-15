numbers = input().split(", ")
numbers_as_integers = []

for number in numbers:
    current_number = int(number)
    numbers_as_integers.append(current_number)


index = 0
while index < len(numbers_as_integers):
    if numbers_as_integers[index] == 0:
        element_to_move = numbers_as_integers.pop(index)
        numbers_as_integers.append(element_to_move)
    else:
        index += 1

print(numbers_as_integers)
