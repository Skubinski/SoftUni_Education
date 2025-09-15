from collections import deque
chocolate = input().split(", ")
milk = deque(input().split(", "))

milkshakes = 0

while not milkshakes == 5:
    if not milk or not chocolate:
        break

    last_chocolate = int(chocolate.pop())

    first_milk = milk.popleft()

    if last_chocolate <= 0 or int(first_milk) <= 0:
        if last_chocolate <= 0:
            milk.appendleft(first_milk)
            continue
        if int(first_milk) <= 0:
            chocolate.append(str(last_chocolate))
            continue



    if int(last_chocolate) == int(first_milk):
        milkshakes += 1

    else:
        milk.append(first_milk)

        last_chocolate -= 5
        chocolate.append(str(last_chocolate))

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")
if chocolate:
    print(f"Chocolate: {", ".join(chocolate)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {", ".join(milk)}")
else:
    print("Milk: empty")

