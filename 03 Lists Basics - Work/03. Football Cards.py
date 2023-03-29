cards = input().split()

first_team_sent_off_players = []
second_team_sent_off_players = []

should_terminate = False

for card in cards:
    if card in first_team_sent_off_players or card in second_team_sent_off_players:
        continue

    cards_args = card.split("-")
    team_name = cards_args[0]
    player_number = cards_args[1]

    is_first_team = team_name == "A"

    if is_first_team:
        first_team_sent_off_players.append(card)
    else:
        second_team_sent_off_players.append(card)

    if len(first_team_sent_off_players) > 4 or len(second_team_sent_off_players) > 4:
        should_terminate = True
        break

initial_player_counter = 11
first_team_final_players_count = initial_player_counter - len(first_team_sent_off_players)
second_team_final_players_count = initial_player_counter - len(second_team_sent_off_players)
print(f"Team A - {first_team_final_players_count}; Team B - {second_team_final_players_count}")
if should_terminate:
    print("Game was terminated")