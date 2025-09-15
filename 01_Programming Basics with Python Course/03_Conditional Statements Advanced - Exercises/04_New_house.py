
type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0
discount = 0


if type_flowers == "Roses":
    price = 5
    if number_flowers > 80:
        discount = 0.10

elif type_flowers == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        discount = 0.15
elif type_flowers == "Tulips":
    price = 2.80
    if number_flowers > 80:
        discount = 0.15
elif type_flowers == "Narcissus":
    price = 3
    if number_flowers < 120:
        discount = -0.15
elif type_flowers == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        discount = -0.20
ammount = price * number_flowers * (1-discount)


if ammount <= budget:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - ammount:.2f} leva left.")
else:
    print(f"Not enough money, you need {ammount - budget:.2f} leva more.")