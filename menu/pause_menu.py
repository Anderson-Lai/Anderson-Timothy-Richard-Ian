import pygame
from draw_text import draw_text


def generate_pause_menu(screen) -> None:
    screen.fill((0, 0, 0))

    # paused title
    draw_text(screen, "PAUSED", "sfnsmono", 70, (0, 240, 60), True, (265, 125))

    # resume game button
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 275, 350, 100), 0, 20)
    draw_text(screen, "Resume", "sfnsmono", 40, (255, 255, 255), False, (320, 300))

    # restart button
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 400, 350, 100), 0, 20)
    draw_text(screen, "Restart", "sfnsmono", 40, (255, 255, 255), False, (310, 425))

    # main menu button
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 525, 350, 100), 0, 20)
    draw_text(screen, "Main Menu", "sfnsmono", 40, (255, 255, 255), False, (290, 550))