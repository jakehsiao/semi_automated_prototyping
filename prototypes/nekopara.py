from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../nekopara/"

def nekopara_setup():
    cards = read_cards(game_dir+"cards.txt")

    decks = [
        Deck([Card(c) for c in cards], 0, "d"),
        Deck([], 2, "h"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "init = map sh d | 5 d",
            "R = 5 mv h d | init",
                                ]),
    }

    return board