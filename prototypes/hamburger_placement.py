from .Card import Card, read_cards
from .Deck import Deck
from .functions_maker import functions_maker
import random

game_dir = "../hamburger_placement/"

def generate_mission():
    values = {
    "臭豆腐": 2,
    "腐乳": 3,
    "柠檬": 4,
    "老干妈": 5,
    }
    formats = [[0,1,2], [1,1,1], [0,2,2]]
    foods = random.sample(values.keys(), 3)
    
    objects = []
    for i,t in enumerate(random.choice(formats)):
        for j in range(t):
            objects.append(foods[i])
            
    total_value = sum([values[o] for o in objects])
    
    reward_ratio = 0.75 # need tuning
    
    reward_value = total_value * reward_ratio
    
    rewards = [random.choice(list(values))]
    
    if total_value >= 12:
        rewards.append(random.choice(list(values)))
        
    score_value = int(reward_value // 2)
    money_value = reward_value - sum([values[o] for o in rewards])
    money_value = max(int(money_value), 0)
    
    return random.choice("RGB")+" "+str(objects)+" "+str(rewards)+" "+str(money_value)+"块钱 "+str(score_value)+"分"


def hamburger_placement_setup():
    places = read_cards(game_dir+"places.txt")
    bonus = read_cards(game_dir + "bonus.txt")
    skills = read_cards(game_dir + "skills.txt")
    # trades = read_cards(game_dir + "trades.txt")
    #missions = [generate_mission() for i in range(50)]
    #trades = [str(i+1)+":"+j for i,j in enumerate(random.sample(["臭豆腐","腐乳","柠檬","老干妈","分数","临时工"],3))]

    decks = [
        Deck([Card(c) for c in bonus], 0, "bd"),
        Deck([], 2, "bl"),
        Deck([Card(c) for c in skills], 0, "sd"),
        Deck([], 2, "sl"),
        Deck([], 2, "ib"),
        # Deck([Card(c) for c in trades], 0, "td"),
        # Deck([], 2, "tl"),
        # Deck([Card(c) for c in places], 2, "p"),
        # Deck([], 2, "f"),
    ]

    board = {
        "decks": dict([(d.name,d) for d in decks]),
        "functions": functions_maker([
            "d = mv d h",
            "u <x> = mv h <x> e",
            "i <x> = mv h <x> i",
            "c <x> = mv i <x> e",
            "f <x> = mv c1 <x> f | mv c1d c1",
            "g <x> = mv c2 <x> f | mv c2d c2",
            "r = 99 mv i e | d",
            "init = map sh bd sd | 4 mv bd bl | 4 mv sd sl | 2 mv bd ib",
            "R = 99 mv sl sd | 99 mv bl bd | 99 mv ib bd | init",
        ]),
    }

    return board