lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

lost_helmets = lost_fights_count // 2
lost_swords = lost_fights_count // 3
lost_shileds = lost_fights_count // 6
lost_armor = lost_shileds // 2

expenses = lost_swords * sword_price \
          + lost_armor * armor_price \
          + lost_helmets * helmet_price \
          + lost_shileds * shield_price
print(f"Gladiator expenses: {expenses:.2f} aureus")