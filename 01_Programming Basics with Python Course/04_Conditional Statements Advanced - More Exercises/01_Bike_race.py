#input
junior_bicyclist = int(input())
expert_bicyclist = int(input())
trace = input()
total_number_of_participants = junior_bicyclist + expert_bicyclist
#conditions
j_tax = 0
e_tax = 0

if trace == "trail":
    j_tax = 5.50
    e_tax = 7
elif trace == "cross-country":
    j_tax = 8
    e_tax = 9.50
elif trace == "downhill":
    j_tax = 12.25
    e_tax = 13.75
elif trace == "road":
    j_tax = 20
    e_tax = 21.50
total = junior_bicyclist * j_tax + expert_bicyclist * e_tax

if trace == "cross-country":
    if total_number_of_participants >= 50:
        total = total - (total * 0.25)
costs = total - (total * 0.05)
print(f"{costs:.2f}")