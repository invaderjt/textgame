from constants import *
from enemies import *
import random


location_glossary = {
 
    (0,0) : {
        "feature" : "Castle Blackhill",
        "environment" : "Settlement",
        "encounter" : None,
        "arrival" : "The walls of Castle Blackhill are as imposing as they are comforting.",
        "search" : [
            "There are several people to talk to and businesses to visit.",
            ["Blacksmith", "Merchant", "Priest"],
        ]
    },
    (0,1) : {
        "feature" : "Road",
        "environment" : "Forest",
        "encounter" : ["Bugbear", "Goblin"],
        "arrival" : "The road North of the castle is falling apart. The bricks are cracked and displaced, scarred from conflict.",
        "search" : None
    },
    (2,3) : {
        "feature" : "Old Mines",
        "environment" : "Forest",
        "encounter" : ["Ogre", "Bugbear", "Hobgoblin", "Goblin", "Goblin"],
        "arrival" : "The old mines are overrun with goblins. They're trying to get into the entrance. You hear someone calling for help from within!",
        "search" : [
            "A dwarf is trying to crawl out of the collapsed mine entrance. He's bruised and covered in filth. Could this be the blacksmith's son?",
            ["Survivor"],
        ]
    }
    
    
}




def encounter_difficulty():
    pass




class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.key = (x, y)
        self.discovered = False
        if self.key in location_glossary:
            data = location_glossary[self.key]
            self.feature = data["feature"]
            self.environment = data["environment"]
            self.encounter = data["encounter"]
            self.search = data["search"]
            self.arrival = data["arrival"]
        else:
            self.feature = random.choice(features)
            self.environment = random.choice(environments)
            self.encounter = []
            for _ in range(random.choice(range(1,4))):
                self.encounter.append(random.choice(encounters))
            self.search = None
            self.arrival = f"You reach a {self.environment}. There is a {self.feature} nearby."



    def __repr__(self):
        return f"{str(self.x)}${str(self.y)}${str(self.discovered)}"
    
    def arrive(self):
        print(self.arrival)
        if not self.discovered:
            self.discovered = True
            if self.encounter is not None:run_encounter(self.encounter)

    def distance_from_blackhill(self) -> int:
        hyp = abs(self.x) ** 2 + abs(self.y) ** 2
        return int(hyp ** 0.5)

locations = {}

def generate_world():
    for i in range(-WORLD_SIZE, WORLD_SIZE + 1):
        for j in range(-WORLD_SIZE, WORLD_SIZE + 1):
            locations[(i, j)] = Location(i, j)

features = [
    "Ruined Structure",
    "Cabin",
    "Camp",
    "Giant Tree",
]
environments = [
    "Road",
    "Forest",
    "River",
    "Field",
]
encounters = [
    "Goblin",
    "Hobgoblin",
    "Bugbear",
    "Ogre",
]