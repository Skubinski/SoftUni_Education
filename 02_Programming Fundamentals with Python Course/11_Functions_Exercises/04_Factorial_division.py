def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_and_divide(factorial_num1, factorial_num2):
    if factorial_num2 == 0:
        print("Division by zero is undefined.")
        return

    result1 = factorial(factorial_num1)
    result2 = factorial(factorial_num2)

    division_result = result1 / result2

    print(f"{division_result:.2f}")

# Example usage:
num1 = int(input())
num2 = int(input())
calculate_and_divide(num1, num2)
