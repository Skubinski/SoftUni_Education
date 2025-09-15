#input
days = int(input()) - 1
room = input()
rate = input()
price = 0
total = 0
if room == "room for one person":
    price = 18
elif room == "apartment":
    price = 25
else:
    price = 35
total = price * days

if room == "apartment":
    if days < 10:
        total = total - (total * 0.30)
    elif 10 <= days <= 15:
        total = total - (total * 0.35)
    else:
        total = total - (total * 0.50)
elif room == "president apartment":
    if days < 10:
        total = total - (total * 0.10)
    elif 10 <= days <= 15:
        total = total - (total * 0.15)
    else:
        total = total - (total * 0.20)

if rate == "positive":
    total = total + (total * 0.25)
else:
    total = total - (total * 0.10)
print(f"{total:.2f}")

