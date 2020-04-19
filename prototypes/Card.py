class Card:
    
    def __init__(self, content="", state=None):
        self.content = content
        
        # about that bug
        self.state = state if state else {}

    def __str__(self):
        if self.state:
            return self.content+" "+str(self.state)
        else:
            return self.content


def read_cards(fn):
    with open(fn) as f:
         return f.read().split("\n")