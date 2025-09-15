numbers = input().split()
numbers_absolute = []

for num in numbers:
    current_num = float(num)
    numbers_absolute.append(abs(current_num))
print(numbers_absolute)