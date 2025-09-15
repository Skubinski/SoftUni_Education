from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

crafted_products = {}

while materials and magic:
    last_material = materials.pop()
    first_magic = magic.popleft()

    if last_material == 0 and first_magic == 0:
        continue
    if last_material == 0:
        magic.appendleft(first_magic)
        continue
    if first_magic == 0:
        materials.append(last_material)
        continue

    total_magic = last_material * first_magic

    if total_magic == 150:
        crafted_products["Doll"] = crafted_products.get("Doll", 0) + 1
    elif total_magic == 250:
        crafted_products["Wooden train"] = crafted_products.get("Wooden train", 0) + 1
    elif total_magic == 300:
        crafted_products["Teddy bear"] = crafted_products.get("Teddy bear", 0) + 1
    elif total_magic == 400:
        crafted_products["Bicycle"] = crafted_products.get("Bicycle", 0) + 1
    elif total_magic < 0:
        materials.append(last_material + first_magic)
    else:
        materials.append(last_material + 15)

crafted = ("Doll" in crafted_products and "Wooden train" in crafted_products) or \
          ("Teddy bear" in crafted_products and "Bicycle" in crafted_products)

if crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for product in sorted(crafted_products):
    print(f"{product}: {crafted_products[product]}")
