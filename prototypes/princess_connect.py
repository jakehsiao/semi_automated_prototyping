from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../princess_connect/"

def princess_connect_setup():
    cards = read_cards(game_dir+"cards.txt")
    actions = read_cards(game_dir+"actions.txt")

    decks = [
        Deck([Card(c) for c in actions+actions], 0, "d"),
        Deck([Card(c) for c in cards+cards], 0, "D"),
        Deck([], 2, "EF"),
        Deck([], 2, "F"),
        Deck([], 2, "h"),
        Deck([], 2, "H"),
        Deck([], 1, "e"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "D = mv D H",
            "i <x> = mv h <x> f | s f -1 h 0",
            "I <x> = mv h <x> f | s f -1 a 0",
            "adv <x> = t f <x> a 1",
            "dec <x> = t f <x> a -1",
            "u <x> = mv h <x> e",
            "a <x> = s f <x> h 1",
            "r <x> = s f <x> h 0",
            # "R = mapd r f",
            "R = 99 mv F D | 99 mv EF D | 99 mv H D | 99 mv h d",
            "e = mv E F",
            "k <x> = mv F <x> ED",
            "l <x> = mv f <x> e",
            "initb = map sh d D | 5 d | 3 mv D F | 3 mv D EF",
            "init = map sh d D | 5 D ",
                                ]),
    }

    return board