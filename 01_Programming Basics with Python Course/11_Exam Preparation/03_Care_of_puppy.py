#input
food = float(input()) * 1000
command = input()
total_food = 0
while command != "Adopted":
    food_quantity = int(command)
    total_food += food_quantity
    command = input()
if total_food <= food:
    print(f"Food is enough! Leftovers: {int(food - total_food)} grams.")
else:
    print(f"Food is not enough. You need {int(total_food - food)} grams more.")