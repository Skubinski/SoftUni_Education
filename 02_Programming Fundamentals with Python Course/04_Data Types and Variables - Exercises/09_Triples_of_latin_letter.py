letters = int(input())
for first_number in range(letters):
    for second_number in range(letters):
        for third_number in range(letters):
            print(f"{chr(97+first_number)}{chr(97+second_number)}{chr(97+third_number)}")