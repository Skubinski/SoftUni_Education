TICKET_PRICE = 150
items = input().split("|")
budget = float(input())
purchased_items_price = []
profit = 0
for i in items:
    item, price = i.split("->")
    item_price = float(price)
    if item == "Clothes" and item_price <= 50:
        if budget < item_price:
            continue
        else:
            budget -= item_price
            purchased_items_price.append(item_price)

    elif item == "Shoes" and item_price <= 35:
        if budget < item_price:
            continue
        else:
            budget -= item_price
            purchased_items_price.append(item_price)
    elif item == "Accessories" and item_price <= 20.5:
        if budget < item_price:
            continue
        else:
            budget -= item_price
            purchased_items_price.append(item_price)

for k in range(len(purchased_items_price)):
    old_price = purchased_items_price[k]
    new_price = purchased_items_price[k] + (purchased_items_price[k] * 0.4)
    purchased_items_price[k] = f"{new_price:.2f}"
    profit += new_price  - old_price
for j in range(len(purchased_items_price)):
    current_price = float(purchased_items_price[j])
    budget += current_price
for l in purchased_items_price:
    print(l, end=" ")
print(f"\nProfit: {profit:.2f}")
if budget >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")
