#input
number = int(input())
for num in range(1111, 10000):
    number_as_string = str(num)
    is_special = True
    for _, digit in enumerate(number_as_string):
        current_digit = int(digit)

        if current_digit == 0:
            is_special = False
            break
        if not number % current_digit == 0:
            is_special = False
            break
    if is_special:
        print(f"{num}", end= " ")