from .Card import Card
from .Deck import Deck
from .functions_maker import functions_maker

dominion_kingdoms = [
    "Cellar 2: +1 A, Discard X, Draw X",
    "Village 3: +2 A, +1 C",
    "Workshop 3: Gain a card costing up to 4",
    "Remodel 4: Trash a card, gain a card costing up to 2 more",
    "Smithy 4: +3 C",
    "Throne room 4: Play an action card twice",
    "Lab 5: +2 C, +1 A",
    "Market 5: +1 C, +1 A, +1 B, +1 $",
]

dominion_basics = [
    "$2 3",
    "$3 6",
    "3VP 5",
    "6VP 8",
]

dominion_starting_hand = ["$1" for i in range(7)]+["1VP" for i in range(3)]

def dominion_setup():
    decks = {}
    for i,k in enumerate(dominion_kingdoms):
        decks["C"+str(i)] = Deck([Card(k) for i in range(10)], 1, "C"+str(i)) # EH: name should not be represented twice, actually list to dict is a solution for this
    for i,b in enumerate(dominion_basics):
        decks["B"+str(i)] = Deck([Card(b) for i in range(8)], 1, "B"+str(i))
    decks["d"] = Deck([Card(b) for b in dominion_starting_hand], 0, "d")
    decks["h"] = Deck([], 2, "h")
    decks["e"] = Deck([], 1, "e")
    decks["stat"] = Deck([Card("Stat", {"Round":0, "Score":0})], 1, "stat")

    board = {
        "decks": decks,
        "functions": functions_maker([
            "d = mv d h",
            "u <x> = mv h <x> e",
            "f = 99 mv h e | 5 d | t stat 0 Round 1",
            "r = 99 mv e d | sh d",
            "R <x> = r | <x> d",
            "b <x> = mv <x> e",
            "sc = t stat 0 Score 1",
        ])
    }

    return board