from card import create_deck
from player import Player

deck = create_deck()

number_of_players = 2

players = []
for player in range(number_of_players):
    players.append(Player(input("Enter player name, please: ")))

# --------

players[0].pick_cards(deck)
players[1].pick_cards(deck)

round_winner = []

first_player = players[0]
second_player = players[1]

for round_index in range(3):
    first_player.play_card()
    second_player.play_card()

    if first_player.played_cards[round_index].rank() < second_player.played_cards[round_index].rank():
        round_winner.append(first_player)
        first_player = players[0]
        second_player = players[1]
    else:
        round_winner.append(second_player)
        first_player = players[1]
        second_player = players[0]

    if round_winner.count(players[0]) >= 2:
        print("\nThe winner is {}!!!".format(players[0].name))
        break

    if round_winner.count(players[1]) >= 2:
        print("\nThe winner is {}!!!".format(players[1].name))
        break
