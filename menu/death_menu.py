import pygame
from game.score import draw_score
from textDrawing.draw_text import draw_text


def death_menu(screen, high_score, current_score):
    screen.fill((0, 0, 0))

    draw_text(screen, "You died!", "sfnsmono", 65, (255, 255, 255), False, (300, 150))

    draw_text(screen, f"All time high-score: {high_score}", "sfnsmono", 45, (255, 255, 255), False, (215, 250))
    draw_text(screen, f"Your score: {current_score}", "sfnsmono", 45, (255, 255, 255), False, (280, 325))

    # return to main menu
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 450, 380, 100), 0, 20)
    draw_text(screen, "Main Menu", "sfnsmono", 40, (255, 255, 255), False, (335, 475))
