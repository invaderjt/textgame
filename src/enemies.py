from combat import calculate_damage, check_if_hit
import player_info
from bones import *
from formatters import *

class Enemy():
    def __init__(self, name: str, hp: int, mp: int, attack: int, armor: int, speed: int, loot: list):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.armor = armor
        self.speed = speed
        self.loot = loot

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
        active_enemies.append(Enemy(enemy_info["name"], enemy_info["hp"], enemy_info["mp"], enemy_info["attack"], enemy_info["armor"], enemy_info["speed"], enemy_info["loot"]))
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




enemy_glossary = {
    "Goblin" : {
        "name" : "Goblin",
        "hp" : 5,
        "mp" : 0,
        "attack" : 2,
        "armor" : 1,
        "speed" : 4,
        "loot" : []
    },
    "Ogre" : {
        "name" : "Ogre",
        "hp" : 10,
        "mp" : 0,
        "attack" : 3,
        "armor" : 2,
        "speed" : 2,
        "loot" : []
    }
}