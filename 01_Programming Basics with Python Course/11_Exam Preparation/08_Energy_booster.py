price = 0
discount = 0
total_money = 0
fruit = input()
set_size = input()
number_sets = int(input())
if set_size == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20
elif set_size == "big":
    if fruit == "Watermelon":
        price = 28.70
    elif fruit == "Mango":
        price = 19.60
    elif fruit == "Pineapple":
        price = 24.80
    elif fruit == "Raspberry":
        price = 15.20
if set_size == "big":
    total_money = 5 * price
else:
    total_money = 2 * price
sets_price = total_money * number_sets
if 400 <= sets_price <= 1000:
    discount = 0.15
elif sets_price > 1000:
    discount = 0.5
final_price = sets_price - (sets_price * discount)
print(f"{final_price:.2f} lv.")



