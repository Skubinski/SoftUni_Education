def rounding (numbers):
    rounded_list = []
    for num in numbers:
        rounded_list.append(round(float((num))))
    return rounded_list
numbers = input().split()
print(rounding(numbers))
