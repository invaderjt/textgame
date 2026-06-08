import random


def calculate_damage(raw_damage: int, armor: int) -> int:
    damage = raw_damage * (1 - armor / 100)
    return int(damage)

def check_if_hit(speed, target_speed):  
    hit_chance = max(0.1, 0.7 + (speed - target_speed) * 0.1)
    return random.random() < hit_chance
    