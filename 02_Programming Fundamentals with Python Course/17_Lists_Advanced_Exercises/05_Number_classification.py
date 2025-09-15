def positive_numbers (list):
    positive = [num for num in list if int(num) >= 0]
    return ', '.join(positive)

def negative_numbers (list):
    negative = [num for num in list if int(num) < 0]
    return ', '.join(negative)

def even_numbers (list):
    even = [num for num in list if int(num) % 2 == 0]
    return ', '.join(even)

def odd_numbers (list):
    odd = [num for num in list if int(num) % 2 != 0]
    return ', '.join(odd)

numbers = input().split(', ')


print(f"Positive: {positive_numbers(numbers)} ")
print(f"Negative: {negative_numbers(numbers)} ")
print(f"Even: {even_numbers(numbers)} ")
print(f"Odd: {odd_numbers(numbers)} ")
