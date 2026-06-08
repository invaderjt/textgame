from progression import *
from bones import *
import player_info
from locations import *
from formatters import *


def main():
    choice = intro_block().lower()
    if choice == "load":
        loaded = False
        while not loaded:
            loaded = load_game()
    else:
        name, method, god, job = introduction()
        player_info.player = player_info.Player(name, method, god, job)
        player_info.player.get_starting_gear(player_info.player.job)
        generate_world()
    while True:
        what_next()



main()