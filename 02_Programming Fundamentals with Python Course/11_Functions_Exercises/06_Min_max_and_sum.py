def minimum_number (numbers):

    return min(numbers)

def maximum_number (numbers):
    return max(numbers)

def sum_of_numbers (numbers):
    return sum(numbers)
number = input().split()
number_as_int = []
for i in number:
    number_as_int.append(int(i))
print(f"The minimum number is {minimum_number(number_as_int)}")
print(f"The maximum number is {maximum_number(number_as_int)}")
print(f"The sum number is: {sum_of_numbers((number_as_int))}")