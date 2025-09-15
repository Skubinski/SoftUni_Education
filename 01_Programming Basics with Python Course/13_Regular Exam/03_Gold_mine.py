#input

locations = int(input())
for _ in range(locations):
    total = 0
    average_gold_per_day = float(input())
    days = int(input())
    for day in range(days):
        gold_earned = float(input())
        total += gold_earned
    average = total / days
    if average >= average_gold_per_day:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {average_gold_per_day - average:.2f} gold.")