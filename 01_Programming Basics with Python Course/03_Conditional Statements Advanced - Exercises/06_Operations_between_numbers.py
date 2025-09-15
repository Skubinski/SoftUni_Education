#input
n1 = int(input())
n2 = int(input())
math_operator = input()
sum = 0
even_or_odd = ""
#conditions
if math_operator == "+":
    sum = n1 + n2
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {sum} - {even_or_odd}")
elif math_operator == "-":
    sum = n1 - n2
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {sum} - {even_or_odd}")
elif math_operator == "*":
    sum = n1 * n2
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {sum} - {even_or_odd}")
elif math_operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {n1 / n2:.2f}")
elif math_operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")


