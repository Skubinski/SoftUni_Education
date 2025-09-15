dessert = input()
quantity = int(input())
day_before_christmas = int(input())

cake_price = 24
souffle_price = 6.66
baklava_price = 12.60

discount_15 = 15
discount_25 = 25
additional_discount = 10

price = 0

if dessert == "Cake":
    if day_before_christmas <= 15:
        price = cake_price * quantity
    else:
        price = 28.70 * quantity
elif dessert == "Souffle":
    if day_before_christmas <= 15:
        price = souffle_price * quantity
    else:
        price = 9.80 * quantity
elif dessert == "Baklava":
    if day_before_christmas <= 15:
        price = baklava_price * quantity
    else:
        price = 16.98 * quantity

if day_before_christmas <= 22:
    if 100 <= price <= 200:
        price -= price * (discount_15 / 100)
    elif price > 200:
        price -= price * (discount_25 / 100)

if day_before_christmas <= 15:
    price -= price * (additional_discount / 100)

print(f"{price:.2f}")
