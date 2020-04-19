from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../hamburger/"

def hamburger_setup():
    c1 = read_cards(game_dir+"card1.txt")
    c2 = read_cards(game_dir+"card2.txt")
    m1 = read_cards(game_dir+"materials.txt")

    decks = [
        Deck(sum([[Card(c) for c in m1] for i in range(3)],[]), 0, "d"),
        Deck([], 1, "e"),
        Deck([Card(random.choice("RGB")+" "+c) for c in c2], 0, "c2d"),
        Deck([], 2, "c2"),
        Deck([Card(random.choice("RGB")+" "+c) for c in c1], 0, "c1d"),
        Deck([], 2, "c1"),
        Deck([], 2, "h"),
        Deck([], 2, "i"),
        Deck([], 2, "f"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "u <x> = mv h <x> e",
            "i <x> = mv h <x> i",
            "c <x> = mv i <x> e",
            "f <x> = mv c1 <x> f | mv c1d c1",
            "g <x> = mv c2 <x> f | mv c2d c2",
            "r = 99 mv i e | d",
            "init = map sh c1d c2d d | 4 mv c1d c1 | 3 mv c2d c2 | 3 d",
        ]),
    }

    return board