from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../nekopara_lcg/"

def nekopara_setup():
    cards = read_cards(game_dir+"cards.txt")
    missions = read_cards(game_dir+"missions.txt")
    customers = read_cards(game_dir+"customers.txt")

    decks = [
        Deck([Card("面包") for i in range(20)], 1, "F0"),
        Deck([Card("茶饮") for i in range(20)], 1, "F1"),
        Deck([Card("奶茶") for i in range(20)], 1, "F2"),
        Deck([Card("蛋糕") for i in range(20)], 1, "F3"),
        Deck([Card(random.choice("RGB")+" "+c) for c in customers], 0, "od"),
        Deck([], 1, "of"),
        Deck([], 2, "ol"),
        Deck([Card(c) for c in missions], 0, "md"), 
        Deck([Card(random.choice("RGB")+" "+c) for c in cards], 0, "cd"),
        Deck([], 2, "cl"),
        Deck(sum([["面粉","鸡蛋","牛奶","茶叶"] for i in range(10)], []), 0, "fd"),
        Deck([], 2, "fl"),
        Deck([], 2, "ml"),
        Deck([], 2, "h"),
        Deck([], 2, "ar"),
        Deck([], 1, "e"),
        Deck([Card("Data", {"Money":0, "Score":0})], 1, "data"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "b <x> = mv cl <x> ar | mv cd cl",
            "p <x> = mv fl <x> h | mv fd fl",
            "d = mv fd h",
            "mk <x> = mv <x> h",
            "c = t data 0 Money -1",
            "a = t data 0 Money 1",
            "sc = t data 0 Score 1",
            "u <x> = mv h <x> e",
            "f <x> = mv ol <x> of | mv od ol",
            "r = mv cl e | mv cd cl",
            "dr = 3 mv cl e | 3 mv cd cl",
            "ch <x> = mv cl <x> h | dr",
            "dp <x> = mv h <x> ar",
            "SD = map sh fd md cd od | 3 mv cd cl | 2 mv md ml",
            "SG = 2 mv cl e | 5 mv fd fl | 5 mv od ol | s data 0 Money 3",
            "init = map sh fd md cd od | 5 mv cd cl | 5 mv fd fl | 5 mv od ol | s data 0 Money 3 | 2 mv md ml"
        ]),
    }

    return board