from math import floor
W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

number_of_tournaments = int(input())
starting_points = int(input())

total_points = starting_points
total_wins = 0
for _ in range(number_of_tournaments):
    stage = input()
    if stage == "W":
        total_points += W_POINTS
        total_wins += 1

    elif stage == "F":
        total_points += F_POINTS
    elif stage == "SF":
        total_points += SF_POINTS

average_points = (total_points - starting_points) / number_of_tournaments
percents = (total_wins / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percents:.2f}%")