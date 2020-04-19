from run import run
from prototypes.dominion import dominion_setup
from prototypes.hamgurger import hamburger_setup
from prototypes.nekopara import nekopara_setup
from prototypes.arknights import arknights_setup

if __name__ == "__main__":

    #board = dominion_setup()
    #board = hamburger_setup()
    board = arknights_setup()

    run(board)