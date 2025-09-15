number_1 = int(input())
number_2 = int(input())

for numbers in range(number_1, number_2 + 1):

    first_digit = int(str(numbers)[0])
    second_digit = int(str(numbers)[1])
    third_digit = int(str(numbers)[2])
    fourth_digit = int(str(numbers)[3])
    if first_digit % 2 == 0 or second_digit % 2 == 0 or third_digit % 2 == 0 or fourth_digit % 2 == 0:
        continue
    print(numbers, end= " ")





