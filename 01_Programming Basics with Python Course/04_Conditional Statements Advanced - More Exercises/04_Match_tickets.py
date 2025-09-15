#input
budget = float(input())
category = input()
number_of_people = int(input())
#conditions
price = 0
transport = 0
if category == "VIP":
    price = 499.99 * number_of_people
else:
    price = 249.99 * number_of_people

if 1 <= number_of_people <= 4:
    transport = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport = budget * 0.60
elif 10 <= number_of_people <= 24:
    transport = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport = budget * 0.40
else:
    transport = budget * 0.25
total = price + transport
if total <= budget:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")