#input
month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_price *= 0.95
    elif 14 < nights:
        studio_price *= 0.70
        apartment_price *= 0.90

elif month == "June" or month =="September":
    studio_price = 75.20
    apartment_price = 68.70
    if 14 < nights:
        studio_price *= 0.80
        apartment_price *= 0.90

elif month == "July" or month =="August":
    studio_price = 76
    apartment_price = 77
    if 14 < nights:
        apartment_price *= 0.90
total_ap = nights * apartment_price
total_s = nights * studio_price
print(f"Apartment: {total_ap:.2f} lv.")
print(f"Studio: {total_s:.2f} lv.")
