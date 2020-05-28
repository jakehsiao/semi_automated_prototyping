from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../arknights2/"

def arknights2_setup():
    pack_ver1 = read_cards(game_dir+"cards.txt")
    enemies = read_cards(game_dir+"enemies.txt")
    places = read_cards(game_dir+"places.txt")
    bonus = read_cards(game_dir+"bonus.txt")
    objects = read_cards(game_dir+"objects.txt")
    missions = read_cards(game_dir+"missions.txt")

    pack_basic = read_cards(game_dir+"pack_basic.txt")
    pack_cycle1 = read_cards(game_dir+"pack_cycle1.txt")
    pack_upgrades = read_cards(game_dir+"pack_upgrades.txt")

    cards = []
    cards += pack_ver1
    #cards += pack_basic
    #cards += pack_cycle1
    #cards += pack_upgrades

    # process cards
    for i in range(len(cards)):
        if "/" in cards[i]:
            material = random.choice("铁铜煤石")
            cards[i] += " {}+{}".format(material, material)
        cards[i] += " " + random.choice(["<><>", "<>[]", "[][]"])

    decks = [
        Deck([Card(c+" ({}) ".format(random.randrange(4))) for c in enemies+enemies+enemies], 1, "D"),
        Deck([Card(c) for c in cards+cards], 0, "d"),

        Deck([], 2, "F1"),
        Deck([Card(places[0])], 2, "f1"),
        Deck([], 2, "F2"),
        Deck([Card(places[1])], 2, "f2"),
        Deck([], 2, "F3"),
        Deck([Card(places[2])], 2, "f3"),
        Deck([], 2, "F4"),
        Deck([Card(places[3])], 2, "f4"),

        Deck([], 2, "h"),
        Deck([], 1, "e"),
        Deck([], 1, "E"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "i1 <x> = mv h <x> f1 | s f1 -1 h 0",
            "i2 <x> = mv h <x> f2 | s f2 -1 h 0",
            "i3 <x> = mv h <x> f3 | s f3 -1 h 0",
            "i4 <x> = mv h <x> f4 | s f4 -1 h 0",
            "l1 <x> = mv f1 <x> e",
            "l2 <x> = mv f2 <x> e",
            "l3 <x> = mv f3 <x> e",
            "l4 <x> = mv f4 <x> e",
            "u <x> = mv h <x> e",
            "a1 <x> = s f1 <x> h 1",
            "a2 <x> = s f2 <x> h 1",
            "a3 <x> = s f3 <x> h 1",
            "a4 <x> = s f4 <x> h 1",
            "R <x> = setd <x> h 0",
            "I1 = mv D F1",
            "I2 = mv D F2",
            "I3 = mv D F3",
            "I4 = mv D F4",
            "L1 <x> = mv F1 <x> E",
            "L2 <x> = mv F2 <x> E",
            "L3 <x> = mv F3 <x> E",
            "L4 <x> = mv F4 <x> E",
            "init = map sh d D | 8 d",
                                ]),
    }

    return board