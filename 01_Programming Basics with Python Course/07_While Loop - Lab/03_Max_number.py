import sys
max_number = -sys.maxsize
numbers = input()
while numbers != "Stop":
    current_number = int(numbers)
    if current_number > max_number:
        max_number = current_number
    numbers = input()
print(max_number)


