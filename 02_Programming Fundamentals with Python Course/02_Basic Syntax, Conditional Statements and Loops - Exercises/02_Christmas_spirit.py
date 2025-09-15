quantity = int(input())
days = int(input())
total_money = 0
total_spirit = 0
ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLAND_PRICE = 3
TREE_LIGHTS_PRICE = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_money += ORNAMENT_SET_PRICE * quantity
        total_spirit += 5
    if day % 3 == 0:
        total_money += quantity * (TREE_GARLAND_PRICE + TREE_SKIRT_PRICE)
        total_spirit += 13
    if day % 5 == 0:
        total_money += quantity * TREE_LIGHTS_PRICE
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_money += TREE_LIGHTS_PRICE + TREE_GARLAND_PRICE + TREE_SKIRT_PRICE
if days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_money}")
print(f"Total spirit: {total_spirit}")