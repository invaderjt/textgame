from utils import get_player_input
import player_info
from formatters import *
import items


def talk_to_npc(npc: str):
    speaker = npc_dialogue[npc.lower()]
    next_line = speaker["last_said"] + 1
    if speaker["quest"] is not None and next_line == speaker["quest"][1]:
        acceptance = quest_prompt(speaker["dialogue"][next_line])
        if acceptance == "accept":
            text_box(speaker["quest_accept"])
            if speaker["quest_accept_item"] is not None:
                player_info.player.add_to_bag(speaker["quest_accept_item"])
                print(f"{npc.title()} gave you a {speaker["quest_accept_item"]}")
            player_info.player.current_quests.add(speaker["quest"][0])
        else:
            text_box(speaker["quest_decline"])
        speaker["last_said"] += 1
    elif speaker["quest_turn_in"] is not None and next_line == speaker["quest_turn_in"][1]:
        if speaker["quest_turn_in"][0] in player_info.player.current_quests:
            player_info.player.current_quests.remove(speaker["quest_turn_in"][0])
        player_info.player.completed_quests.add(speaker["quest_turn_in"][0])
        text_box(speaker["dialogue"][next_line])
        speaker["last_said"] += 1
        print(f"~~ Quest '{speaker["quest_turn_in"][0]}' completed! ~~")
    elif next_line >= len(speaker["dialogue"]):
        text_box(speaker["exhausted"])
    else:
        text_box(speaker["dialogue"][next_line])
        speaker["last_said"] += 1
    choice = get_player_input("", ["Continue", "Goodbye"])
    if choice.lower() == "goodbye":
        player_info.player.state = "exploring"

def quest_prompt(prompt: str) -> str:
    text_box(prompt)
    return get_player_input("", ["Accept", "Decline"]).lower()


intro_blurb = "You stand at the gate of Castle Blackhill, the last bastion of mankind. The ancient structure is surrounded by a vast, uncharted wilderness that has been permanently scarred by the aftermath of the Elemental Surge. Food runs low and those capable of venturing outside the walls are few. The burden falls to you, brave hero, to be the champion of those who remain."


npc_dialogue = {
    "blacksmith" : {
        "dialogue": [
            "Well, if it isn't the new guy. I'd love to help you out, but I've got a bit of a problem. My son went to fetch me some wood from the forest North of here yesterday morning, and he hasn't found his way back yet. He's a good kid, but I'm worried something out there might have got to him. If you can find him and bring him home, I'll give you any weapon you like from my shop.",
        ],
        "quest" : ["Blacksmith's Son", 0],
        "quest_accept" : "Thanks a lot. Take this to help. And be careful; it's dangerous out there.",
        "quest_accept_item" : "Potion",
        "quest_decline" : "Bah, typical. You adventurers always think you're too busy to help the common folk.",
        "quest_turn_in" : None,
        "last_said" : -1,
        "exhausted" : "Best of luck out there."
    },
    "priest" : {
        "dialogue" : [
            "Hello traveler. I'm sure your journey through our scarred wilderness has been challenging. You can rest assured that you're safe within these walls.",
            "The presence of The Life Song is strong here."
        ],
        "quest" : None,
        "quest_turn_in" : None,
        "last_said" : -1,
        "exhausted" : "May you walk in the light of The Life Song."
    },
    "merchant" : {
        "dialogue" : [
            "Afraid I don't have much to offer right now. The Elemental Surge really put a damper on business. I used to have all sorts of things to sell, but now I'm lucky if I can get my hands on some food and basic supplies.",
            "If you find any interesting items out there, bring them to me. I might be able to trade you for something useful."
        ],
        "quest" : None,
        "quest_turn_in" : None,
        "last_said" : -1,
        "exhausted" : "Come again soon!"
    },
    "survivor" : {
        "dialogue" : [
            "Is someone there? Please, come help me out of here.",
            "Thank you so much. I need to get this wood back to my father before he gets worried.",
            "Oh. He's already worried? Can you tell him you found me heroically fending off goblins from some innocent puppies? The truth is too embarrassing."
        ],
        "quest" : None,
        "quest_turn_in" : ["Blacksmith's Son", 1],
        "last_said" : -1,
        "exhausted" : f"I need to get back to the Castle quickly! Thanks again for saving me, traveler."
    },
}


