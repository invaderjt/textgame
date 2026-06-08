import items
from formatters import separator
from combat import calculate_damage, check_if_hit



class Player():
    def __init__(self, name, method, god, job):
        self.name = name
        self.method = method
        self.god = god
        self.job = job
        self.quests_completed = set()
        self.bag = []
        self.gear: dict[str, items.Item | None] = {
            "Head" : None,
            "Body" : None,
            "Hands" : None,
            "Feet" : None,
            "Main_Hand" : None,
            "Off_Hand" : None,
            "Extra" : None
        }
        self.level = 1
        self.max_hp = 100
        self.current_hp = self.max_hp
        self.xp = 0
        self.max_mp = 0
        self.current_mp = self.max_mp
        self.atk_bonus = 0
        self.spl_bonus = 0
        self.speed = 3
        self.state = "exploring"
        self.in_combat = False
        self.position = (0,0)
        self.prev_position = (0,0)
        self.armor = 0
        self.current_quests = set()
        self.completed_quests = set()
        match self.job:
            case "Knight":
                self.max_hp += 5
                self.heal_to_full()
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
        new_item = items.item_glossary[item]
        match new_item["type"]:
            case "weapon":
                acquired = items.Weapon(quantity, new_item["name"], new_item["weight"], new_item["slot"], new_item["damage"], new_item["dmg_type"])
            case "armor":
                acquired = items.Armor(quantity, new_item["name"], new_item["weight"], new_item["slot"], new_item["armor"], new_item["effect"])
            case _:
                acquired = items.Item(quantity, new_item["name"], new_item["weight"])
        for object in self.bag:
            if object == acquired:
                object.quantity += quantity
                return
        self.bag.append(acquired)

    def get_starting_gear(self, job: str):
        match job:
            case "Knight":
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
                pass
            case "Monk":
                pass
            case "Priest":
                pass
            case "Acolyte":
                pass
            case "Mystic":
                pass


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
        target_slot = self.gear[slot]
        if target_slot is not None:
            current = self.find_item(target_slot.name)
            assert current is not None
            self.bag[current].equipped = False
            self.armor -= target_slot.armor if isinstance(target_slot, items.Armor) else 0
            print(f"{target_slot.name} unequipped.")
        self.gear[slot] = self.bag[equipping]
        self.bag[equipping].equipped = True
        self.armor += self.bag[equipping].armor if isinstance(self.bag[equipping], items.Armor) else 0
        print(f"{name} equipped.")

    def unequip_item(self, slot: str):
        target_slot = self.gear[slot]
        if target_slot is None:
            print(f"No item equipped in {slot}.")
            return
        current = self.find_item(target_slot.name)
        assert current is not None
        self.bag[current].equipped = False
        self.armor -= target_slot.armor if isinstance(target_slot, items.Armor) else 0
        print(f"{target_slot.name} unequipped.")
        self.gear[slot] = None

    def show_bag(self):
        separator("-")
        print ("Your bag contains:")
        if len(self.bag) == 0:
            print("Nothing")
            return
        for item in self.bag:
            if item.equipped:
                print(f"{item.name} (equipped)")
            elif item.quantity > 1:
                print(f"{item.name} x{item.quantity}")
            else:
                print(item.name)
        separator("-")

    def show_status(self):
        separator("-")
        print(f"{self.name} the {self.job}")
        print(f"Level: {self.level}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"MP: {self.current_mp}/{self.max_mp}")
        print(f"XP: {self.xp}")
        print(f"Attack Bonus: {self.atk_bonus}")
        print(f"Spell Bonus: {self.spl_bonus}")
        print(f"Speed: {self.speed}")
        print(f"Armor: {self.armor}")
        separator("-")


    def attack_enemy(self, enemy):
        damage = self.atk_bonus
        if self.gear["Main_Hand"] is not None and isinstance(self.gear["Main_Hand"], items.Weapon):
            damage += self.gear["Main_Hand"].damage
        if check_if_hit(self.speed, enemy.speed):
            actual_damage = calculate_damage(damage, enemy.armor)
            enemy.hp -= actual_damage
            print(f"You hit the {enemy.name} for {actual_damage} damage.")
        else:
            print("You missed!")


player = Player("not set", "not set", "not set", "not set")

