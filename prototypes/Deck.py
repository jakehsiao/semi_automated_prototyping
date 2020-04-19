import random

# deck and cl is actually one thing

class Deck:
    
    def __init__(self, deck=[], available=0, name="d"):
        self.deck = deck
        self.available = available # available: 0 not available, 1 only top, 2 full
        self.name = name
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def __repr__(self):
        cards = ""
        if self.available == 0:
            cards = ""
        elif self.available == 1 and self.deck:
            cards = "TopCard: {}".format(str(self.deck[0]))
        else:
            cards = "Cards: \n{}".format("\n".join([str(i)+": "+str(c) for i,c in enumerate(self.deck)]))
        return "Deck: {}\n{}\n".format(self.name, cards)