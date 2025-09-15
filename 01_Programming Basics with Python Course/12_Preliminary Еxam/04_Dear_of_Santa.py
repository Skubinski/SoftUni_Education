#input
from math import ceil, floor
days = int(input())
food = int(input())
food_first_dear = float(input())
food_second_dear = float(input())
food_third_dear = float(input())
#calculations
food_needed_for_first_dear = food_first_dear * days
food_needed_for_second_dear = food_second_dear * days
food_needed_for_third_dear = food_third_dear * days
total_food_needed = food_needed_for_first_dear + food_needed_for_second_dear + food_needed_for_third_dear
if total_food_needed <= food:
    print(f"{floor(food - total_food_needed)} kilos of food left.")
else:
    print(f"{ceil(total_food_needed - food)} more kilos of food are needed.")
