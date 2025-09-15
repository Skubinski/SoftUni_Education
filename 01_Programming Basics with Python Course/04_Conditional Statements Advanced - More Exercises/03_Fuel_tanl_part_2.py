#input
fuel = input()
quantity = float(input())
card = input()
#conditions
price = 0

if fuel == "Gas":
    price = 0.93
    if card == "Yes":
        price = price - 0.08
elif fuel == "Gasoline":
    price = 2.22
    if card == "Yes":
        price = price - 0.18
elif fuel == "Diesel":
    price = 2.33
    if card == "Yes":
        price = price - 0.12
total = price * quantity
if 20 <= quantity <= 25:
    total = total - (total * 0.08)
elif quantity > 25:
    total = total - (total * 0.10)
print(f"{total:.2f} lv.")
