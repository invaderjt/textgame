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
    "re",
    "quests",
]

input_queue = ""
last_input = ""

def universal_input(command: str) -> None:
    match command:
        case "exit":
            if player_info.player.name != "not set":
                save_prompt = get_player_input("Save first?", ["Yes", "No"]).lower()
                if save_prompt == "yes":
                    universal_input("save")
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
        case "re":
            global input_queue
            global last_input
            input_queue = last_input
        case "quests":
            print(f"Current Quests: {player_info.player.current_quests}")
            print(f"Completed Quests: {player_info.player.completed_quests}")


def try_again():
    global input_queue
    text = [
        "What was that..?",
        "I didn't get that...",
        "Try that again...",
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
            if prompt != "":
                response = input(prompt + "\n" + " | ".join(options) + "\n")
            else:
                response = input(" | ".join(options) + "\n")
            if response.lower() != "re":
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
        quick_options = []
        if response.lower() not in lower_options:
            if len(response) == 1:
                for option in lower_options:
                    if option.startswith("the "):
                        quick_options.append(option[4])
                    else:
                        quick_options.append(option[0])
                if response.lower() in quick_options:
                    return lower_options[quick_options.index(response.lower())]
            try_again()
        else:
            return response



