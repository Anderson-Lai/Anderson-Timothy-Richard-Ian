import pygame
from textDrawing.draw_text import draw_text

"""
start game button
permanent upgrades (the shop)
settings
"""

def generate_menu(screen):
    screen.fill((0, 0, 0))

    # game title
    draw_text(screen, "SPACE", "sfnsmono", 85, (0, 240, 60), True, (260, 155))
    draw_text(screen, "COLONIZERS", "sfnsmono", 85, (0, 240, 60), True, (160, 225))

    # play game
    pygame.draw.rect(screen, (255, 255, 237), pygame.Rect(175, 550, 450, 150))
    draw_text(screen, "PLAY", "sfnsmono", 65, (0, 0, 0), True, (320, 582.5))

    # open shop
    pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(50, 575, 100, 100))
    shop_icon = pygame.image.load("./gameImages/shopping-cart.png")
    smaller_shop_icon = pygame.transform.scale(shop_icon, (82.5, 82.5))
    screen.blit(smaller_shop_icon, (58, 583))

    # open settings
    pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(650, 575, 100, 100))
    settings_icon = pygame.image.load("./gameImages/settings_icon.png")
    smaller_settings_icon = pygame.transform.scale(settings_icon, (85, 85))
    screen.blit(smaller_settings_icon, (658.5, 582.5))