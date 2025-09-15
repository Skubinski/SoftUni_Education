def calculator (operator , num_1, num_2):
    if operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2
    elif operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return int(num_1 / num_2)
operator = input()
num_1 = int(input())
num_2 = int(input())
print(calculator(operator, num_1, num_2))