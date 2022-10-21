from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../conspiracy/"

# def unpack_cards(cards_raw):
#     cards = []

#     for c in cards_raw:
#         for i in range(int(c[-1])):
#             cards.append(c[:-1])

#     return cards

def conspiracy_setup():
    cards = read_cards(game_dir+"cards.txt")
    objects = read_cards(game_dir+"objects.txt")
    publics = read_cards(game_dir+"publics.txt")

    decks = [
        Deck([Card(c) for c in objects], 0, "od"),
        Deck([Card(c) for c in publics], 0, "pd"),
        Deck([Card(c) for c in cards], 0, "d"),
        Deck([], 2, "pl"),
        Deck([], 2, "ol"),
        Deck([], 2, "h"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "init = map sh od pd d | 1 mv od ol | 1 mv pd pl | 6 mv d h",
            "R = 99 mv h d | 99 mv ol od | 99 mv pl pd | init ",
        ]),
    }

    return board

