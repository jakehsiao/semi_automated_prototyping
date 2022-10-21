from run import run
from prototypes.dominion import dominion_setup
from prototypes.hamgurger import hamburger_setup
from prototypes.nekopara import nekopara_setup
from prototypes.arknights import arknights_setup
from prototypes.arknights2 import arknights2_setup
from prototypes.arknights3 import arkfights_setup
from prototypes.arknights_roguelike import arknights_roguelike_setup
from prototypes.arknights_pvp import arknights_pvp_setup
from prototypes.hamburger_placement import hamburger_placement_setup
from prototypes.princess_connect import princess_connect_setup
from prototypes.record_company import record_company_setup
from prototypes.conspiracy import conspiracy_setup
from prototypes.point_salad import point_salad_setup
from prototypes.village_rules import village_rules_setup
from prototypes.draft_loop import draft_loop_setup

if __name__ == "__main__":

    #board = dominion_setup()
    # board = hamburger_setup()
    # board = nekopara_setup()
    #board = arknights_setup()
    # board = arknights2_setup()
    # board = arkfights_setup()
    # board = arknights_roguelike_setup()
    # board = arknights_pvp_setup()
    # board = hamburger_placement_setup()
    # board = princess_connect_setup()
    #board = record_company_setup()
    # board = conspiracy_setup()
    #board = point_salad_setup()
    board = village_rules_setup()
    # board = draft_loop_setup()

    run(board)