# #input

trip_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

# prices

PUZZLE = 2.60
DOLL = 3.00
BEAR = 4.10
MINION = 8.20
TRUCK = 2.00

number_of_toys = number_trucks + number_minions + number_bears + number_dolls + number_puzzles


discount = 0
if number_of_toys >= 50:
    discount = 0.25

total_revenue = number_puzzles * PUZZLE + number_dolls * DOLL + number_bears * BEAR \
    + number_minions * MINION + number_trucks * TRUCK


total_revenue_with_discount = total_revenue * (1 - discount)

rent_cost = total_revenue_with_discount * 0.10

final_revenue = total_revenue_with_discount - rent_cost


if final_revenue >= trip_price:
    print(f"Yes! {final_revenue - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - final_revenue:.2f} lv needed.")