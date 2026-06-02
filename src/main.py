from progression import *
from bones import *
import player_info
from locations import *


def main():
    choice = intro_block().lower()
    if choice == "load":
        loaded = False
        while not loaded:
            loaded = load_game()
    else:
        name, method, god, job = introduction()
        player_info.player = player_info.Player(name, method, god, job)
        generate_world()
    while True:
        next()



main()