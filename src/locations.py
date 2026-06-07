from constants import *
from enemies import *


location_glossary = {
 
    (0,0) : {
        "feature" : "Castle Blackhill",
        "climate" : "Temperate",
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
        "climate" : "Temperate",
        "environment" : "Forest",
        "encounter" : ["Bugbear", "Goblin"],
        "arrival" : "The road North of the castle is falling apart. The bricks are cracked and displaced, scarred from conflict.",
        "search" : None
    }
    
    
}


settlements_glossary = {
    
    "Castle Blackhill" : {
        "NPCs" : [
            "Blacksmith",
            "Merchant",
            "Priest",
        ],
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
            self.climate = data["climate"]
            self.environment = data["environment"]
            self.encounter = data["encounter"]
            self.search = data["search"]

    def __repr__(self):
        return f"{str(self.x)}${str(self.y)}${str(self.discovered)}"
    
    def arrive(self):
        print(location_glossary[self.key]["arrival"])
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