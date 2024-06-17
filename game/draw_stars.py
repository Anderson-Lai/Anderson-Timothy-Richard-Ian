import pygame
from random import randint
from game.start_game import Position

class Star(Position):
    def __init__(self, x: int, y: int, acceleration: int) -> None:
        super().__init__(x, y)
        self.acceleration = acceleration

stars: list[Star] = []

def draw_stars(screen, frame_counter: int) -> None:
    if frame_counter % 4 == 0 :
        stars.append(Star(randint(-280, 280), randint(-15, 15), 2))
    for n in range(len(stars) - 1, -1, -1):
    
        pygame.draw.rect(screen, (255, 255, 255), (round(stars[n].pos_x) + 310, round(stars[n].pos_y), 5, 5))

        if stars[n].pos_y >= 800: 
            stars.pop(n)
        else: 
            stars[n].pos_y += 5 * stars[n].acceleration
            stars[n].acceleration *= 1.01