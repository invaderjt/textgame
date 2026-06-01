from formatters import *
from constants import *
from dialogue import *
import random

def try_again():
    text = [
        "What was that?"
        "I didn't get that."
        "Try that again."
        "That's not right..."
        "That won't work..."
    ]
    print(random.choice(text))

def intro_block():
    separator("~")
    separator("-")
    print("\n")
    print(center_text("Castle Blackhill"))
    print(center_text("A text adventure by InvaderJT"))
    print("\n")
    separator("-")
    separator("~")

def get_player_input(prompt: str, options: list[str] | None = None) -> str:
    while True:
        if options is None:
            return input(prompt + "\n")
        response = input(prompt + "\n" + " | ".join(options) + "\n")
        lower_options = []
        for option in options:
            lower_options.append(option.lower())
        if response.lower() not in lower_options:
            try_again()
        else:
            return response
    
def assign_job(method: str, god: str) -> str | None:
    if method == "Sword":
        if god == "The Life Song":
            return "Knight"
        elif god == "The Woundkeeper":
            return "Warrior"
        elif god == "The Sagelight":
            return "Monk"
    elif method == "Spell":
        if god == "The Life Song":
            return "Priest"
        elif god == "The Woundkeeper":
            return "Acolyte"
        elif god == "The Sagelight":
            return "Mystic"
    else:
        raise ValueError("Could not assign job.")


def introduction():
    intro_block()
    dialogue(intro_blurb)
    confirmed = False
    while not confirmed:
        name = get_player_input("What is your name?")
        method = get_player_input("What do you bring to battle?", ["Sword", "Spell"]).title()
        god = get_player_input("Who do you look to?", ["The Life Song", "The Woundkeeper", "The Sagelight"]).title()
        job = assign_job(method, god)
        confirmation = get_player_input(f"Your are {name}, {job} of {god}.", ["Confirm", "Restart"]).title()
        if confirmation == "Confirm":
            confirmed = True
        else:
            continue
    return name, method, god, job

def dialogue(text):
    text_box(text)