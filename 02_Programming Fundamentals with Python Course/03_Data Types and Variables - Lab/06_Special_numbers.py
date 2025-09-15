# Input: Read an integer n
n = int(input())

# Iterate through numbers from 1 to n and check if they are special
for number in range(1, n + 1):
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))

    # Check if the sum is 5, 7, or 11
    special = digit_sum in (5, 7, 11)

    print(f"{number} -> {special}")

