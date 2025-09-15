#input
film_budget = float(input())
number_of_statists = int(input())
price_per_clothes_for_one_statist = float(input())

#given
decor_budget = film_budget * 0.10
clothes_budget = number_of_statists * price_per_clothes_for_one_statist
total_money_needed = decor_budget + clothes_budget


if total_money_needed <= film_budget and number_of_statists < 150:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_money_needed:.2f} leva left.")

elif total_money_needed <= film_budget and number_of_statists >= 151:
    clothes_with_discount = clothes_budget - (clothes_budget * 0.10)
    total_money_needed = decor_budget + clothes_with_discount
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_money_needed:.2f} leva left.")

else:
    clothes_with_discount = clothes_budget - (clothes_budget * 0.10)
    total_money_needed = decor_budget + clothes_with_discount
    print("Not enough money!")
    print(f"Wingard needs {total_money_needed - film_budget:.2f} leva more.")