#input
n = int(input())
left_number = 0
right_number = 0
for number in range(n * 2):
    current_number = int(input())
    if number < n:
        left_number += current_number
    else:
        right_number += current_number
if left_number == right_number:
    print(f"Yes, sum = {left_number}")
else:
    difference = abs(left_number - right_number)
    print(f"No, diff = {difference}")
