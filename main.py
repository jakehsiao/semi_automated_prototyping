from run import run
from prototypes.dominion import dominion_setup
from prototypes.hamgurger import hamburger_setup
from prototypes.nekopara import nekopara_setup
from prototypes.arknights import arknights_setup
from prototypes.hamburger_placement import hamburger_placement_setup
from prototypes.princess_connect import princess_connect_setup
from prototypes.record_company import record_company_setup
from prototypes.conspiracy import conspiracy_setup
from prototypes.point_salad import point_salad_setup

if __name__ == "__main__":

    #board = dominion_setup()
    #board = hamburger_setup()
    board = arknights_setup()
    #board = hamburger_placement_setup()
    #board = princess_connect_setup()
    #board = record_company_setup()
    #board = conspiracy_setup()
    #board = point_salad_setup()

    run(board)