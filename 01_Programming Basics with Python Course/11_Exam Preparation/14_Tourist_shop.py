# #input
total_money = 0
total_products = 0
budget = float(input())
money_left = budget
while True:
    command = input()
    if command == "Stop":
        break
    product = command
    product_price = float(input())
    if money_left < product_price:
        break
    total_products += 1
    money_left -= product_price

    if total_products % 3 == 0:
        product_price /= 2
    total_money += product_price


if command == "Stop":
    print(f"You bought {total_products} products for {total_money:.2f} leva.")
elif money_left < product_price:
    print(f"You don't have enough money!")
    print(f"You need {product_price - money_left:.2f} leva!")

