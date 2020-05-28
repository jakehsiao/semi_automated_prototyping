from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../conspiracy/"

def unpack_cards(cards_raw):
    cards = []

    for c in cards_raw:
        for i in range(int(c[-1])):
            cards.append(c[:-1])

    return cards

def conspiracy_setup():
    cards_raw = read_cards(game_dir+"cards.txt")
    objects = read_cards(game_dir+"objects.txt")

    basic = unpack_cards(cards_raw[:2])
    operations = unpack_cards(cards_raw[2:])

    random.shuffle(operations)
    operations = operations[:27]

    cards = basic + operations

    decks = [
        Deck([Card(c) for c in objects], 0, "od"),
        Deck([Card(c) for c in cards], 0, "D"),
        Deck([], 0, "d"),
        Deck([], 2, "ol"),
        Deck([], 2, "h"),
        Deck([], 2, "f"),
        Deck([], 1, "e"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "init = map sh od D | 2 mv od ol | 7 mv D h",
            "r = 99 mv h D | sh D | 7 mv D h",
                    ]),
    }

    return board

