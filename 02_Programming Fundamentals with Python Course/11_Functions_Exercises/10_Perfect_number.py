def is_perfect_number(number):
    if number <= 0:
        return "It's not so perfect."

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    if divisor_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

# Example usage:
input_number = int(input())
result = is_perfect_number(input_number)
print(result)
