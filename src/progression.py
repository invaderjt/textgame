from formatters import *
from constants import *
from dialogue import *


def intro_block():
    separator("~")
    separator("-")
    print("\n")
    print(center_text("Castle Blackhill"))
    print(center_text("A text adventure by InvaderJT"))
    print("\n")
    separator("-")
    separator("~")

def get_player_input(prompt: str):
    response = input(prompt)
    
    
    return

def introduction():
    intro_block()
    dialogue(intro_blurb)
    confirm = False
    while not confirm:
        name = input("What is your name?")
        method = ch

def dialogue(text):
    text_box(text)