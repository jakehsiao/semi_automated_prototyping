from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../arknights/"

def arknights_setup():
    cards = read_cards(game_dir+"cards.txt")
    enemies = read_cards(game_dir+"enemies.txt")

    decks = [
        Deck([Card(c) for c in enemies+enemies], 0, "E"),
        Deck([], 1, "ED"),
        Deck([Card(c) for c in cards+cards], 0, "d"),
        Deck([], 2, "score"),
        Deck([], 2, "F"),
        Deck([], 2, "f"),
        Deck([], 2, "h"),
        Deck([], 1, "e"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "i <x> = mv h <x> f | s f -1 h 1",
            "I <x> = mv h <x> f | s f -1 a 0",
            "adv <x> = t f <x> a 1",
            "dec <x> = t f <x> a -1",
            "u <x> = mv h <x> e",
            "a <x> = s f <x> h 1",
            "r <x> = s f <x> h 0",
            "R = mapd r f",
            "e = mv E F",
            "k <x> = mv F <x> ED",
            "l <x> = mv f <x> e",
            "init = map sh d E | 6 d",
                                ]),
    }

    return board