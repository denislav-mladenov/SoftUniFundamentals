# cards = input().split(", ")
# commands = int(input())
# index_range = len(cards)
#
# for i in range(commands):
#     command = input().split(", ")
#     action = command[0]
#     if action == "Add":
#         card = command[1]
#         if card not in cards:
#             cards.append(card)
#             print("Card successfully added")
#         else:
#             print("Card is already in the deck")
#     elif action == "Remove":
#         card = command[1]
#         if card not in cards:
#             print("Card not found")
#         else:
#             cards.remove(card)
#             print("Card successfully removed")
#     elif action == "Remove At":
#         index = int(command[1])
#         if index < 0 or index > index_range:
#             print("Index out of range")
#         else:
#             card = cards[index]
#             cards.pop(index)
#             print("Card successfully removed")
#     elif action == "Insert":
#         index = int(command[1])
#         card = command[2]
#         if index < 0 or index > index_range:
#             print("Index out of range")
#         elif card not in cards:
#             cards.insert(index, card)
#             print("Card successfully added")
#         else:
#             print("Card is already in the deck")
#
# print(", ".join(cards))


def add(cards, card):
    if card in cards:
        print("Card is already in the deck")
    else:
        cards.append(card)
        print("Card successfully added")


def remove(cards, card):
    if card in cards:
        cards.remove(card)
        print("Card successfully removed")
    else:
        print("Card not found")


def remove_at(cards, index):
    if index < 0 or index >= len(cards):
        print("Index out of range")
    else:
        cards.pop(index)
        print("Card successfully removed")


def insert(cards, index, card):
    if index < 0 or index > len(cards):
        print("Index out of range")
    elif card in cards:
        print("Card is already added")
    else:
        cards.insert(index, card)
        print("Card successfully added")


cards = input().split(", ")
num_commands = int(input())


for i in range(num_commands):
    command = input().split(", ")
    if command[0] == "Add":
        add(cards, command[1])
    elif command[0] == "Remove":
        remove(cards, command[1])
    elif command[0] == "Remove At":
        remove_at(cards, int(command[1]))
    elif command[0] == "Insert":
        insert(cards, int(command[1]), command[2])


print(", ".join(cards))
