import pygame
from modifications.getting.get_upgrade_state import get_upgrade_state

def num_lives(gameDifficulty: str) -> int:
    lives = 0
    if gameDifficulty == "hard":
        lives += 1
    elif gameDifficulty == "normal":
        lives += 3
    elif gameDifficulty == "easy":
        lives += 5
    
    if get_upgrade_state("extraLife"):
        lives += 1

    return lives

def draw_removed_hearts(screen, lives:int) -> int:
    heart_colour = (255, 0, 0)
    heart_radius = 10
    for i in range(lives):
        pygame.draw.circle(screen, heart_colour, ((625+(heart_radius/2))+heart_radius*2.65*i, 175), heart_radius)