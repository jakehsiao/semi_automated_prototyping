from parsing import simple_parsing

def run(board):
    rounds = 0
    while True:
        print("\n## Round:", rounds)
        print()

        for d in board["decks"]:
            print(board["decks"][d])

        command = input()

        try:
            simple_parsing(command, board["decks"], board["functions"])
        except Exception as e:
            print("There's an error:", e)
        rounds += 1