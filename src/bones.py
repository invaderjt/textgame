import random
import sys
import os
from formatters import *
import player_info
import locations



universal_commands = [
    "exit",
    "save",
    "whoami"
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



def save_game() -> None:
    plyr = player_info.player
    save_data = ""
    save_data += add_to_save_data(plyr.name)
    save_data += add_to_save_data(plyr.method)
    save_data += add_to_save_data(plyr.god)
    save_data += add_to_save_data(plyr.job)
    for key in locations.locations:
        save_data += add_to_save_data(str(locations.locations[key]))
    with open(f"./saves/{plyr.name.lower()}.txt", "w") as file:
        file.write(save_data)


def add_to_save_data(data: str) -> str:
    return data + "#&\n"


def load_game() -> bool:
    name = get_player_input("What was your name?").lower()
    if not os.path.isfile(f"./saves/{name}.txt"):
        print("Adventurer not found")
        return False
    with open(f"./saves/{name}.txt", "r") as file:
        save_data = file.read()
    data = save_data.split("#&\n")
    player_info.player = player_info.Player(data[0], data[1], data[2], data[3])
    for line in data[4:]:
        info = line.split("$")
        if len(info) == 3:
            locations.locations[info[0],info[1]] = locations.Location(info[0],info[1])
            locations.locations[info[0],info[1]].discovered = info[2]
    print(f"Welcome back, {player_info.player.name}!")
    return True


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
        

