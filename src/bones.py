import random
import sys
import os
from formatters import *
import player_info
import locations
import items



universal_commands = [
    "exit",
    "save",
    "whoami",
    "bag",
]

def universal_input(command: str) -> None:
    match command:
        case "exit":
            save_prompt = get_player_input("Save first?", ["Y", "N"]).lower()
            if save_prompt == "y":
                save_game()
            sys.exit()
        case "save":
            save_game()
        case "whoami":
            plyr = player_info.player
            print(f"You are {plyr.name}, {plyr.job} of {plyr.god}")
        case "bag":
            player_info.player.show_bag()


def save_game() -> None:
    plyr = player_info.player
    save_data = ""
    save_data += add_to_save_data(plyr.name)
    save_data += add_to_save_data(plyr.method)
    save_data += add_to_save_data(plyr.god)
    save_data += add_to_save_data(plyr.job)
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
    print(f"Welcome back, {player_info.player.name}!")
    return True

def str_to_bool(value: str) -> bool:
    return value == "True"


def try_again():
    text = [
        "What was that?",
        "I didn't get that.",
        "Try that again.",
        "That's not right...",
        "That won't work..."
    ]
    print(random.choice(text))


def get_player_input(prompt: str, options: list[str] | None = None) -> str:
    separator("-")
    while True:
        if options is None:
            response = input(prompt + "\n")
            if response.lower() not in universal_commands:
                if not response.isalnum():
                    try_again()
                    continue
                return response
            universal_input(response.lower())
            continue
        response = input(prompt + "\n" + " | ".join(options) + "\n")
        lower_options = []
        for option in options:
            lower_options.append(option.lower())
        if response.lower() not in lower_options and response.lower() not in universal_commands:
            try_again()
        else:
            if response.lower() in universal_commands:
                universal_input(response.lower())
            else:
                return response
        

