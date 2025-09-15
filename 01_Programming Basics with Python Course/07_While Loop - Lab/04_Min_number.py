import sys
min_number = sys.maxsize
numbers = input()
while numbers != "Stop":
    current_number = int(numbers)
    if current_number < min_number:
        min_number = current_number
    numbers = input()
print(min_number)


