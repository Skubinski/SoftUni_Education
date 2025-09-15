divisor = int(input())
boundary = int(input())
numbers = 0
for number in range(divisor, boundary + 1):
    if number % divisor == 0 and number <= boundary and number > 0:
           numbers = number

print(numbers)
