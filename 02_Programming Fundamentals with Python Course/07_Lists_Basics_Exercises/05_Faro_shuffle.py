cards_deck = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    middle_of_the_deck = len(cards_deck) // 2
    left_part = cards_deck[0:middle_of_the_deck]
    right_part = cards_deck[middle_of_the_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    cards_deck = deck_after_shuffling
print(deck_after_shuffling)