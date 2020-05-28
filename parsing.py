import random
from prototypes.Card import Card

def move(deck1, idx, deck2):
    if deck1.deck:
        deck2.deck.append(deck1.deck.pop(idx))
    else:
        print("No cards!")

def D(r):
    return random.randrange(r)

# "m" needs some parsing, if the second one is not a number, then simply move the top.


# mv d 0 h = dr
# mv h <x> e = u <x>

def parse_function(rule, args):
    macro, expand = rule.split("=")
    macro = macro.split()
    expand = expand.split()
    lookup = {}
    for m,a in zip(macro,args):
        if "<" in m:
            lookup[m] = a
    for i,e in enumerate(expand):
        if e in lookup.keys():
            expand[i] = lookup[e]

    return " ".join(expand)

def simple_parsing(command, decks, functions={}):

    if "|" in command:
        commands = command.split("|")
        for c in commands:
            simple_parsing(c, decks, functions)
        return

    args = command.split()
    times = 1
    if args[0].isdigit():
        times = int(args.pop(0))
    for i in range(times):
        if args[0] == "mv":
            if args[2].isdigit():
                move(decks[args[1]], int(args[2]), decks[args[3]])
            else:
                move(decks[args[1]], 0, decks[args[2]])
        elif args[0] == "sh":
            decks[args[1]].shuffle()
        #elif args[0] == "pr":
        #    print(decks[args[1]].deck[int(args[2])])
        elif args[0] == "add":
            decks[args[1]].deck.append(Card(" ".join(args[2:])))
        elif args[0] == "s":
            decks[args[1]].deck[int(args[2])].state[args[3]] = int(args[4])
        elif args[0] == "t":
            decks[args[1]].deck[int(args[2])].state[args[3]] += int(args[4])
        elif args[0] == "map":
            func = args[1]
            for i in range(2, len(args)):
                simple_parsing(func+" "+args[i], decks, functions)
        elif args[0] == "setd":
            dname = args[1]
            decklen = len(decks[dname].deck)
            attr = args[2]
            val = args[3]
            for i in range(decklen):
                # reversed order prepared for delete operations
                simple_parsing("s {} {} {} {}".format(dname, i, attr, val), decks, functions)
        elif args[0] == "def":
            fn = args[1]
            func = " ".join(args[1:])
            func.replace("&", "|")
            functions[fn] = func
            print("Functions:\n", functions)
        elif args[0] in functions.keys():
            simple_parsing(parse_function(functions[args[0]], args), decks, functions)

# TODO: get the function, and the creation, and can setup without touching the code

if __name__ == "__main__":
    #print(parse_function("u <x> = mv h <x> e", ["u", "3"]))
    print(parse_function("dr = mv d h", ["dr"]))