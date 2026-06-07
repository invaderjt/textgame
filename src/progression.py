from formatters import *
from constants import *
from dialogue import *
from bones import *


# Game Start


def intro_block():
    separator("~")
    separator("-")
    print("\n")
    print(center_text("Castle Blackhill"))
    print(center_text("A text adventure by InvaderJT"))
    print("\n")
    separator("-")
    separator("~")
    return get_player_input("", ["New", "Load", "Exit"])
    
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
    dialogue(intro_blurb)
    confirmed = False
    while not confirmed:
        name = get_player_input("What is your name?")
        method = get_player_input("What do you bring to battle?", ["Sword", "Spell"]).title()
        god = get_player_input("Who do you look to?", ["The Life Song", "The Woundkeeper", "The Sagelight"]).title()
        job = assign_job(method, god)
        confirmation = get_player_input(f"You are {name}, {job} of {god}.", ["Confirm", "Restart"]).title()
        if confirmation == "Confirm":
            confirmed = True
        else:
            continue
    return name, method, god, job

def dialogue(text):
    text_box(text)

