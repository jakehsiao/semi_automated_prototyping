import random

def combiner(command):
    parts = command.split("&")

    return "".join([random.choice(p.split()) for p in parts])

if __name__ == "__main__":
    rules = {}
    while True:
        command = input()
        args = command.split()

        if args[0] == "def":
            rules[args[1]] = " ".join(args[2:])
            print(rules)

        elif args[0] in rules.keys():
            for i in range(int(args[1])):
                print(combiner(rules[args[0]]))