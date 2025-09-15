# import sympy
#
# number = int(input())
# is_prime = False
# if sympy.isprime(number):
#     is_prime = True
#     print(is_prime)
# else:
#     print(is_prime)

number = int(input())

if number <= 1:
    is_prime = False
elif number <= 3:
    is_prime = True
elif number % 2 == 0 or number % 3 == 0:
    is_prime = False
else:

    is_prime = True
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            is_prime = False
            break
        i += 6

if is_prime:
    print(True)
else:
    print(False)
