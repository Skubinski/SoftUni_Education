number_of_orders = int(input())
total = 0
for orders in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    current_ammount = capsule_price * capsules_needed_per_day * days
    print(f"The price for the coffee is: ${current_ammount:.2f}")
    total += current_ammount
print(f"Total: ${total:.2f}")
