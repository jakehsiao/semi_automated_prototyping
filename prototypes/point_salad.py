from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../point_salad/"

def point_salad_setup():
    cards = read_cards(game_dir+"cards.txt")
    random.shuffle(cards)

    decks = [
        Deck([Card(c) for c in cards[:32]], 1, "d1"),
        Deck([Card(c) for c in cards[32:64]], 1, "d2"),
        Deck([Card(c) for c in cards[64:]], 1, "d3"),
        Deck([], 2, "l1"),
        Deck([], 2, "l2"),
        Deck([], 2, "l3"),

        Deck([], 2, "v"),
        Deck([], 2, "s"),
        Deck([], 0, "e"),

    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
           "init = 2 mv d1 l1 | 2 mv d2 l2 | 2 mv d3 l3",
           "u1 = mv l1 0 v | mv d1 l1",
           "u2 = mv l1 1 v | mv d1 l1",
           "u3 = mv l2 0 v | mv d2 l2",
           "u4 = mv l2 1 v | mv d2 l2",
           "u5 = mv l3 0 v | mv d3 l3",
           "u6 = mv l3 1 v | mv d3 l3",
           "i1 = mv d1 0 s",
           "i2 = mv d2 0 s",
           "i3 = mv d3 0 s", # maybe simply add a new param to mv would make this easier, but not now, because that function is not utilized
           "e1 = mv l1 0 e | mv d1 l1",
           "e2 = mv l1 1 e | mv d1 l1",
           "e3 = mv l2 0 e | mv d2 l2",
           "e4 = mv l2 1 e | mv d2 l2",
           "e5 = mv l3 0 e | mv d3 l3",
           "e6 = mv l3 1 e | mv d3 l3",
           "r1 = mv d1 0 e",
           "r2 = mv d2 0 e",
           "r3 = mv d3 0 e",
           
                                ]),
    }

    return board