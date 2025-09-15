food = int(input()) * 1000
command = input()
total_food = 0
while command != "Adopted":
    food_eaten = int(command)
    total_food += food_eaten

    command = input()
if total_food <= food:
    print(f"Food is enough! Leftovers: {food - total_food} grams.")
else:
    print(f"Food is not enough. You need {total_food - food} grams more.")
