tournament_days = int(input())
total_money = 0
total_wins = 0
total_losses = 0

for day in range(1, tournament_days + 1):
    daily_money = 0
    wins = 0
    losses = 0

    while True:
        game_result = input()
        if game_result == "Finish":
            break

        if game_result == "win":
            wins += 1
            daily_money += 20
        elif game_result == "lose":
            losses += 1

    if wins > losses:
        daily_money *= 1.10

    total_money += daily_money
    total_wins += wins
    total_losses += losses

if total_wins > total_losses:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
