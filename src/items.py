


class Item():
    def __init__(self, quantity: int, name: str, weight: float, effect: str = None):
        self.name = name
        self.weight = weight
        self.quantity = quantity
        self.effect = effect

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
    def __init__(self, quantity: int, name: str, weight: float, slot: str, damage: int, dmg_type: str, effect: str = None):
        super().__init__(quantity, name, weight, effect)
        self.damage = damage
        self.dmg_type = dmg_type
        self.slot = slot
        self.equipped = False


class Armor(Item):
    def __init__(self, quantity: int, name: str, weight: float, slot: str, armor: int, effect: str):
        super().__init__(quantity, name, weight, effect)
        self.armor = armor
        self.slot = slot
        self.equipped = False

class Consumable(Item):
    def __init__(self, quantity: int, name: str, weight: float, effect: str = None):
        super().__init__(quantity, name, weight, effect)

    def use(self, player):
        print(f"{self.name} has no effect when used.")
        return False


class Potion(Consumable):
    def use(self, player):
        healed = player.max_hp // 2
        new_hp = min(player.current_hp + healed, player.max_hp)
        actual_heal = new_hp - player.current_hp
        player.current_hp = new_hp
        print(f"You drink a Potion and restore {actual_heal} HP.")
        return True


item_glossary = {
    "Potion" : {
        "name" : "Potion",
        "type" : "potion",
        "weight" : 0.5,
        "effect" : "heal_half_max"
    },
    "Sword" : {
        "name" : "Sword",
        "type" : "weapon",
        "weight" : 2.0,
        "slot" : "Main_Hand",
        "damage" : 5,
        "dmg_type" : "physical"
    },
    "Great Sword" : {
        "name" : "Great Sword",
        "type" : "weapon",
        "weight" : 4.0,
        "slot" : "Main_Hand",
        "damage" : 7,
        "dmg_type" : "physical"
    },
    "Shield" : {
        "name" : "Shield",
        "type" : "armor",
        "weight" : 4.0,
        "slot" : "Off_Hand",
        "armor" : 2,
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