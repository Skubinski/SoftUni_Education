events = input().split("|")
total_energy = 100
total_coins = 100
gained_energy = 0
is_opened = True
for event in events:
    event_type, price = event.split("-")
    price = int(price)

    if event_type == "rest":
        current_energy = total_energy
        total_energy += price
        if total_energy > 100:
            total_energy = 100
        gained_energy += total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_type == "order":
        if total_energy >= 30:
            print(f"You earned {price} coins.")
            total_coins += price
            total_energy -= 30
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= price:
            total_coins -= price
            print(f"You bought {event_type}.")
        else:
            is_opened = False
            break
if is_opened:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {event_type}.")


