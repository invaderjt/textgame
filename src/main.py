from progression import *
from bones import *
import player_info



def main():
    choice = intro_block().lower()
    if choice == "load":
        load_game()
    else:
        name, method, god, job = introduction()
        player_info.player = player_info.Player(name, method, god, job)
    while True:
        next()



main()