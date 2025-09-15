team_a_cards = []
team_b_cards = []
is_break = False

team_a_players = 11
team_b_players = 11

cards = input().split()

for card in cards:
    team, player = card.split('-')
    player = int(player)


    if (team == 'A' and player in team_a_cards) or (team == 'B' and player in team_b_cards):
        continue

    if team == 'A':
        team_a_cards.append(player)
        team_a_players -= 1
    else:
        team_b_cards.append(player)
        team_b_players -= 1

    # Check if the game should be terminated
    if team_a_players < 7 or team_b_players < 7:
        is_break = True
        break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if is_break:
    print("Game was terminated")
