import bag



class Player():
    def __init__(self, name, method, god, job):
        self.name = name
        self.method = method
        self.god = god
        self.job = job
        self.quests_completed = set()
        self.bag = []
        self.gear = {
            "Head" : None,
            "Body" : None,
            "Hands" : None,
            "Feet" : None,
            "Main_Hand" : None,
            "Off_Hand" : None,
            "Extra" : None
        }
        self.level = 1
        self.max_hp = 10
        self.current_hp = self.max_hp
        self.xp = 0
        self.max_mp = 0
        self.current_mp = self.max_mp
        self.atk_bonus = 0
        self.spl_bonus = 0
        self.speed = 5
        armor = 0
        match self.job:
            case "Knight":
                self.max_hp += 5
                self.heal_to_full()
                self.add_to_bag("Father's Helm")
                self.add_to_bag("Father's Armor")
                self.add_to_bag("Father's Gloves")
                self.add_to_bag("Father's Boots")
                self.add_to_bag("Sword")
                self.add_to_bag("Shield")
                self.equip_item("Father's Helm", "Head")
                self.equip_item("Father's Armor", "Body")
                self.equip_item("Father's Gloves", "Hands")
                self.equip_item("Father's Boots", "Feet")
                self.equip_item("Sword", "Main_Hand")
                self.equip_item("Shield", "Off_Hand")
            case "Warrior":
                self.atk_bonus += 2
            case "Monk":
                self.speed += 2
            case "Priest":
                self.max_hp += 5
                self.heal_to_full()
            case "Acolyte":
                self.spl_bonus += 2
            case "Mystic":
                self.max_mp += 5
                self.mp_to_full()
            
    def heal_to_full(self):
        self.current_hp = self.max_hp

    def mp_to_full(self):
        self.current_mp = self.max_mp

    def full_restore(self):
        self.heal_to_full()
        self.mp_to_full()

    def add_to_bag(self, item: str, quantity: int = 1):
        thing = bag.item_glossary[item]
        match thing["type"]:
            case "weapon":
                acquired = bag.Weapon(quantity, thing["name"], thing["weight"], thing["slot"], thing["damage"], thing["dmg_type"])
            case "armor":
                acquired = bag.Armor(quantity, thing["name"], thing["weight"], thing["slot"], thing["armor"], thing["effect"])
            case _:
                acquired = bag.Item(quantity, thing["name"], thing["weight"])
        for object in self.bag:
            if object == acquired:
                object.quantity += quantity
                return
        self.bag.append(acquired)

    def find_item(self, name: str) -> int | None:
        index = None
        for i in range(len(self.bag)):
            if self.bag[i].name == name:
                index = i
                break
        return index

    def equip_item(self, name: str, slot: str):
        equipping = self.find_item(name)
        if equipping is None:
            print(f"{name} not in bag.")
            return
        if self.gear[slot] is not None:
            current = self.find_item(self.gear[slot].name)
            self.bag[current].equipped = False
            print(f"{self.gear[slot].name} unequipped.")
        self.gear[slot] = self.bag[equipping]
        self.bag[equipping].equipped = True
        print(f"{name} equipped.")


player = Player("not set", "not set", "not set", "not set")

