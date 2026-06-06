


class Item():
    def __init__(self, quantity: int, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.quantity = quantity

    def acquire(self, amount: int = 1):
        self.quantity += amount

    def lose(self):
        self.quantity -= 1

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.name == other.name
    
    def __repr__(self):
        return f"{self.name}"


class Weapon(Item):
    def __init__(self, quantity: int, name: str, weight: float, slot: str, damage: int, dmg_type: str):
        super().__init__(quantity, name, weight)
        self.damage = damage
        self.dmg_type = dmg_type
        self.slot = slot
        self.equipped = False


class Armor(Item):
    def __init__(self, quantity: int, name: str, weight: float, slot: str, armor: int, effect: str):
        super().__init__(quantity, name, weight)
        self.armor = armor
        self.effect = effect
        self.slot = slot
        self.equipped = False




item_glossary = {
    "Sword" : {
        "name" : "Sword",
        "type" : "weapon",
        "weight" : 2.0,
        "slot" : "Main_Hand",
        "damage" : 1,
        "dmg_type" : "physical"
    },
    "Shield" : {
        "name" : "Shield",
        "type" : "armor",
        "weight" : 4.0,
        "slot" : "Off_Hand",
        "armor" : 1,
        "effect" : None
    },
    "Father's Helm" : {
        "name" : "Father's Helm",
        "type" : "armor",
        "weight" : 2.0,
        "slot" : "Head",
        "armor" : 1,
        "effect": None
    },
    "Father's Armor" : {
        "name" : "Father's Armor",
        "type" : "armor",
        "weight" : 20.0,
        "slot" : "Body",
        "armor" : 2,
        "effect": None
    },
    "Father's Gloves" : {
        "name" : "Father's Gloves",
        "type" : "armor",
        "weight" : 1.0,
        "slot" : "Hands",
        "armor" : 1,
        "effect": None
    },
    "Father's Boots" : {
        "name" : "Father's Boots",
        "type" : "armor",
        "weight" : 5.0,
        "slot" : "Feet",
        "armor" : 1,
        "effect": None
    },
}