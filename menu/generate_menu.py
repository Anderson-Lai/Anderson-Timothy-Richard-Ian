import pygame

"""
start game button
permanent upgrades (the shop)
settings
difficulty button 
"""

def generate_menu(screen):
    screen.fill((0, 0, 0))
    # game title
    game_font_type = "sfnsmono"
    game_font_size = 85
    game_font_bold = True
    game_font_colour = (0, 240, 60)
    game_font = pygame.font.SysFont(game_font_type, game_font_size, game_font_bold)
    # draw game title
    title_top = game_font.render("SPACE", True, game_font_colour)
    title_bottom = game_font.render("INVADERS", True, game_font_colour)
    screen.blit(title_top, (260, 155))
    screen.blit(title_bottom, (185, 225))

    # open shop
    pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(50, 575, 100, 100))
    shop_icon = pygame.image.load("shopping-cart.png")
    smaller_shop_icon = pygame.transform.scale(shop_icon, (82.5, 82.5))
    screen.blit(smaller_shop_icon, (58, 583))

    # open settings
    pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(650, 575, 100, 100))
    settings_icon = pygame.image.load("settings_icon.png")
    smaller_settings_icon = pygame.transform.scale(settings_icon, (85, 85))
    screen.blit(smaller_settings_icon, (658.5, 582.5))

    # start game button
    pygame.draw.rect(screen, (255, 255, 237), pygame.Rect(175, 550, 450, 150))
    play_font_type = "sfnsmono"
    play_font_size = 65
    play_font_bold = True
    play_font_colour = (0, 0, 0)
    play_font = pygame.font.SysFont(play_font_type, play_font_size, play_font_bold)
    play_game_text = play_font.render("PLAY", True, play_font_colour)
    screen.blit(play_game_text, (320, 582.5))
