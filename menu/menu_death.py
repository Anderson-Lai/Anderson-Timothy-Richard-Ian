import pygame
from textDrawing.draw_text import draw_text


def death_menu(screen):
    screen.fill((0, 0, 0))

    draw_text(screen, "You died!", "sfnsmono", 30, (255, 255, 255), True, (150, 50))
    pygame.draw.rect(screen, (0, 0, 200), (275, 350, 250, 150))
