budget = float(input())
kg_flour_price = float(input())
eggs_price = kg_flour_price * 0.75
milk_liter_price = kg_flour_price + (kg_flour_price * 0.25)
bread_counter = 0
current_money_spent = 0
colored_eggs_counter = 0
price_for_one_loaf = kg_flour_price + eggs_price + (milk_liter_price / 4)

while current_money_spent < budget:
    current_money_spent += price_for_one_loaf
    if current_money_spent > budget:
        break
    bread_counter += 1
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter - 2
current_money_spent -= price_for_one_loaf
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs\
 and {budget - current_money_spent:.2f}BGN left.")