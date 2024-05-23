import pygame

def game_settings(screen):
    screen.fill((255, 0, 0))

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))