import os
import locations
import items
from formatters import *
import player_info
from utils import get_player_input
from dialogue import *


def what_next() -> None:
    choice = get_player_input("What will you do?", ["Travel","Search","Camp"])
    match choice.lower():
        case "travel":
            travel()
        case "search":
            search()
        case "camp":
            camp()

def search():
    location = locations.locations[player_info.player.position]
    if location.search is None:
        print("There's nothing interesting here...")
        return
    if isinstance(location.search, list):
        choice = get_player_input("Who do you want to talk to?", location.search[1])
        player_info.player.state = "talking"
        while player_info.player.state == "talking":
            talk_to_npc(choice)
    else:
        print(location.search)

def camp():
    player_info.player.full_restore()
    print("You set up camp and rest for the night. Hopefully you go unnoticed...")

def travel():
    direction = get_player_input("Which way?", ["North", "East", "South", "West"])
    x, y = player_info.player.position
    match direction.lower():
        case "north":
            new_position = (x, y + 1)
        case "east":
            new_position = (x + 1, y)
        case "south":
            new_position = (x, y - 1)
        case "west":
            new_position = (x - 1, y)
    if new_position[0] > WORLD_SIZE or new_position[0] < -WORLD_SIZE or new_position[1] > WORLD_SIZE or new_position[1] < -WORLD_SIZE:
        print("You reach an impassable barrier. You cannot go that way.")
        return
    player_info.player.prev_position = player_info.player.position
    player_info.player.position = new_position
    locations.locations[new_position].arrive()
    

def save_game() -> None:
    plyr = player_info.player
    save_data = ""
    save_data += add_to_save_data(plyr.name)
    save_data += add_to_save_data(plyr.method)
    save_data += add_to_save_data(plyr.god)
    save_data += add_to_save_data(plyr.job)
    save_data += add_to_save_data(str(plyr.position[0]) + "$" + str(plyr.position[1]))
    if not os.path.isdir("./saves"):
        os.mkdir("./saves")
    if not os.path.isdir(f"./saves/{plyr.name.lower()}"):
        os.mkdir(f"./saves/{plyr.name.lower()}")
    with open(f"./saves/{plyr.name.lower()}/save.txt", "w") as file:
        file.write(save_data)
    location_data = ""
    for key in locations.locations:
        location_data += add_to_save_data(str(locations.locations[key]))
    with open(f"./saves/{plyr.name.lower()}/locations.txt", "w") as file:
        file.write(location_data)
    item_data = ""
    for item in plyr.bag:
        if isinstance(item, items.Weapon):
            item_data += add_to_save_data(f"Weapon${item.name}${item.quantity}${item.equipped}")
        elif isinstance(item, items.Armor):
            item_data += add_to_save_data(f"Armor${item.name}${item.quantity}${item.equipped}")
        elif isinstance(item, items.Consumable):
            item_data += add_to_save_data(f"Consumable${item.name}${item.quantity}")
        else:
            item_data += add_to_save_data(f"Item${item.name}${item.quantity}")
    with open(f"./saves/{plyr.name.lower()}/items.txt", "w") as file:
        file.write(item_data)


def add_to_save_data(data: str) -> str:
    return data + "#&\n"


def load_game() -> bool:
    name = get_player_input("What was your name?").lower()
    if not os.path.isfile(f"./saves/{name}/save.txt"):
        print("Adventurer not found")
        return False
    with open(f"./saves/{name}/save.txt", "r") as file:
        save_data = file.read()
    data = save_data.split("#&\n")
    player_info.player = player_info.Player(data[0], data[1], data[2], data[3])
    pos = data[4].split("$")
    player_info.player.position = (int(pos[0]), int(pos[1]))
    with open(f"./saves/{name}/locations.txt", "r") as file:
        location_data = file.read()
    data = location_data.split("#&\n")
    for line in data:
        if line != "":
            info = line.split("$")
            locations.locations[int(info[0]),int(info[1])] = locations.Location(int(info[0]),int(info[1]))
            locations.locations[int(info[0]),int(info[1])].discovered = str_to_bool(info[2])
    with open(f"./saves/{name}/items.txt", "r") as file:
        item_data = file.read()
    data = item_data.split("#&\n")
    for line in data:
        if line != "":
            info = line.split("$")
            match info[0]:
                case "Weapon":
                    player_info.player.add_to_bag(info[1], int(info[2]))
                    if str_to_bool(info[3]):
                        player_info.player.equip_item(info[1], items.item_glossary[info[1]]["slot"])
                case "Armor":
                    player_info.player.add_to_bag(info[1], int(info[2]))
                    if str_to_bool(info[3]):
                        player_info.player.equip_item(info[1], items.item_glossary[info[1]]["slot"])
                case "Item":
                    player_info.player.add_to_bag(info[1], int(info[2]))
                case "Consumable":
                    player_info.player.add_to_bag(info[1], int(info[2]))
    print(f"Welcome back, {player_info.player.name}!")
    return True

def str_to_bool(value: str) -> bool:
    return value == "True"



