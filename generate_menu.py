import pygame

"""
start game button
permanent upgrades (the shop)
settings
difficulty button 

"""
def generate_menu(screen):
    screen.fill((0, 0, 255))

    # open settings
    pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(650, 650, 50, 50))

    # start game button
    pygame.draw.rect(screen, (255, 255, 237), pygame.Rect(190, 650, 380, 75))


