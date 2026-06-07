import random
import sys
from formatters import *
import player_info


universal_commands = [
    "exit",
    "save",
    "whoami",
    "bag",
    "status",
    "r",
]

input_queue = ""
last_input = ""

def universal_input(command: str) -> None:
    match command:
        case "exit":
            if player_info.player.name != "not set":
                save_prompt = get_player_input("Save first?", ["Y", "N"]).lower()
                if save_prompt == "y":
                    import bones
                    bones.save_game()
            sys.exit()
        case "save":
            import bones
            bones.save_game()
        case "whoami":
            plyr = player_info.player
            print(f"You are {plyr.name}, {plyr.job} of {plyr.god}")
        case "bag":
            player_info.player.show_bag()
        case "status":
            player_info.player.show_status()
        case "r":
            global input_queue
            global last_input
            input_queue = last_input


def try_again():
    global input_queue
    text = [
        "What was that?",
        "I didn't get that.",
        "Try that again.",
        "That's not right...",
        "That won't work..."
    ]
    print(random.choice(text))
    input_queue = ""


def get_player_input(prompt: str, options: list[str] = [""]) -> str:
    separator("-")
    global input_queue
    global last_input
    while True:
        if input_queue != "":
            response = input_queue
            input_queue = ""
        else:
            response = input(prompt + "\n" + " | ".join(options) + "\n")
            if response.lower() != "r":
                last_input = response.lower()
        if "," in response:
            response, input_queue = response.split(",", maxsplit=1)
            response = response.strip()
            input_queue = input_queue.strip()
        if response.lower() in universal_commands:
            universal_input(response.lower())
            continue
        if options == [""]:
            if not response.isalnum():
                try_again()
                continue
            return response
        lower_options = []
        for option in options:
            lower_options.append(option.lower())
        if response.lower() not in lower_options:
            try_again()
        else:
            return response



