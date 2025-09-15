#input
minutes_walk = int(input())
number_walks = int(input())
calories = int(input())
total_minutes = minutes_walk * number_walks
total_calories = total_minutes * 5
aim = calories * 0.5
if total_calories >= aim:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")
