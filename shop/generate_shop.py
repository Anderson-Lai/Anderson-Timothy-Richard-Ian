import pygame

"""
items:
ship colour

"doubleShot": False, <- rapidly shooting a second set of bullet after the first
"multiShot": False, <- shooting 3 bullets at the same time
"extraLife": False, <- + 2 lives
"fasterFireRate1": False, <- decrement waiting time
"fasterFireRate2": False,
"fasterFireRate3": False,
"""

def generate_shop(screen) -> None:
    screen.fill((0, 0, 0))