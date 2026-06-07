from combat import calculate_damage, check_if_hit
import player_info
from utils import get_player_input
from formatters import *

class Enemy():
    def __init__(self, name: str, hp: int, mp: int, attack: int, armor: int, speed: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.armor = armor
        self.speed = speed

    def attack_player(self):
        if check_if_hit(self.speed, player_info.player.speed):
            damage = calculate_damage(self.attack, player_info.player.armor)
            player_info.player.current_hp -= damage
            print(f"{self.name} hit you for {damage} damage.")
        else:
            print(f"{self.name} missed!") 


def run_encounter(enemies: list[str]):
    active_enemies = []
    for enemy in enemies:
        enemy_info = enemy_glossary[enemy]
        active_enemies.append(Enemy(enemy_info["name"], enemy_info["hp"], enemy_info["mp"], enemy_info["attack"], enemy_info["armor"], enemy_info["speed"]))
    player_info.player.in_combat = True
    intro_string = "You are confronted by a "
    if len(active_enemies) == 1:
        intro_string += active_enemies[0].name + "!"
    else:
        intro_string += active_enemies[0].name + " and " + str(len(active_enemies) - 1) + " other enemies!"
    print(intro_string)
    while player_info.player.in_combat:
        turn_order = sorted(active_enemies + [player_info.player], key=lambda x: x.speed, reverse=True)
        for entity in turn_order:
            if isinstance(entity, player_info.Player):
                action = get_player_input("What will you do?", ["Attack", "Use Item", "Flee"]).title()
                match action:
                    case "Attack":
                        if len(active_enemies) > 1:
                            target = get_player_input("Which one?", [enemy.name for enemy in active_enemies])
                        else:
                            target = active_enemies[0].name
                        for i in range(len(active_enemies)):
                            if active_enemies[i].name == target.title():
                                target_enemy = active_enemies[i]
                                target_index = i
                                break
                        player_info.player.attack_enemy(target_enemy)
                        if target_enemy.hp <= 0:
                            print(f"You defeated the {target_enemy.name}!")
                            active_enemies.pop(target_index)
                        if len(active_enemies) == 0:
                            print("All enemies slain!")
                            player_info.player.in_combat = False
                            break
                    case "Use Item":
                        print("Not yet implemented.")
                    case "Flee":
                        print("You turn back and flee.")
                        player_info.player.in_combat = False
                        player_info.player.position = player_info.player.prev_position
                        break
            else:
                entity.attack_player()
                if player_info.player.current_hp <= 0:
                    print("You have been slain...")
                    exit()

basic = {
    "hp" : 5,
    "mp" : 0,
    "attack" : 2,
    "armor" : 0,
    "speed" : 2,
}
quick = {
    "hp" : 3,
    "mp" : 0,
    "attack" : 1,
    "armor" : 0,
    "speed" : 5,
}
bruiser = {
    "hp" : 8,
    "mp" : 0,
    "attack" : 4,
    "armor" : 1,
    "speed" : 1,
}
tank = {
    "hp" : 12,
    "mp" : 0,
    "attack" : 2,
    "armor" : 5,
    "speed" : 1,
}


enemy_glossary = {
    "Goblin" : {
        "name" : "Goblin",
        "hp" : quick["hp"],
        "mp" : quick["mp"],
        "attack" : quick["attack"],
        "armor" : quick["armor"],
        "speed" : quick["speed"],
    },
    "Hobgoblin" : {
        "name" : "Hobgoblin",
        "hp" : basic["hp"],
        "mp" : basic["mp"],
        "attack" : basic["attack"],
        "armor" : basic["armor"],
        "speed" : basic["speed"],
    },
    "Bugbear" : {
        "name" : "Bugbear",
        "hp" : bruiser["hp"],
        "mp" : bruiser["mp"],
        "attack" : bruiser["attack"],
        "armor" : bruiser["armor"],
        "speed" : bruiser["speed"]
    },
    "Ogre" : {
        "name" : "Ogre",
        "hp" : tank["hp"],
        "mp" : tank["mp"],
        "attack" : tank["attack"],
        "armor" : tank["armor"],
        "speed" : tank["speed"],
    }
}