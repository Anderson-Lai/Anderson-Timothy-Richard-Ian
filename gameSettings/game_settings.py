import pygame

def game_settings(screen):
    screen.fill((0, 0, 0))

    # sensitivy and difficulty buttons
    # difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 200, 200, 100))

    # sensitivity
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(350, 350, 100, 50))
    # increment sensitivity
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(475, 350, 50, 50))
    # decrement sensitivity
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, 350, 50, 50))

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))