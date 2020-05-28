from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../record_company/"

def record_company_setup():
    singers = read_cards(game_dir+"singers.txt")
    markets = read_cards(game_dir+"markets.txt")
    agents = read_cards(game_dir+"agents.txt")
    upgrades = read_cards(game_dir+"upgrades.txt")
    operations = read_cards(game_dir+"operations.txt")

    decks = [
        Deck([Card(c) for c in singers], 0, "sd"),
        Deck([], 2, "sh"),
        Deck([Card(c) for c in markets], 0, "md"),
        Deck([Card(c) for c in agents], 0, "ad"),
        Deck([Card(c) for c in upgrades], 0, "ud"),
        Deck([], 2, "uh"),
        Deck([Card(c) for c in operations], 0, "od"),
        Deck([], 2, "oh"),
        Deck([], 2, "h"),
        Deck([], 1, "e"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "i <x> = mv h <x> f | s f -1 h 0",
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
            "init = map sh sd od ud md ad | 5 mv ad h | 4 mv sd sh | 4 mv ud uh | 4 mv od oh | 3 mv md h",
                                ]),
    }

    return board