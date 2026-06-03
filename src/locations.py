from constants import *



location_glossary = {
 
    (0,0) : {
        "feature" : "Castle Blackhill",
        "climate" : "Temperate",
        "environment" : "Settlement",
        "encounter" : None
        }
    
    
}


settlements_glossary = {
    
    "Castle Blackhill" : {
        "NPCs" : {
            None
        },
        "Places" : {
            "Hogwarts" : None
        },
    }
}




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

    def __repr__(self):
        return f"{str(self.x)}${str(self.y)}${str(self.discovered)}"

locations = {}

def generate_world():
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            locations[(i, j)] = Location(i, j)