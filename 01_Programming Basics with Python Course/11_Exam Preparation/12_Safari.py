#input
budget = float(input())
litres_needed = float(input())
day = input()
LITRE_PRICE = 2.10
TOUR_MAN_PRICE = 100
discount = 0
#calculations
total_fuel_needed = litres_needed * LITRE_PRICE
#conditions
if day == "Sunday":
    discount = 0.2
elif day == "Saturday":
    discount = 0.1
total_money = total_fuel_needed + TOUR_MAN_PRICE
total_money_with_discount = total_money - (total_money * discount)
if total_money_with_discount <= budget:
    print(f"Safari time! Money left: {budget - total_money_with_discount:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_money_with_discount - budget:.2f} lv.")


