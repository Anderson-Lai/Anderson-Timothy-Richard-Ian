import pygame
from game.score import draw_score


def menudeath(screen, high_score, current_score):
    screen.fill((0, 0, 0))
    font_type = "sfnsmono"
    font_size = 30
    font_bold = False
    font_colour = (255, 255, 255)
    font = pygame.font.SysFont(font_type, font_size, font_bold)

    #draws high score
    hi = font.render(f"ALL TIME HIGH SCORE: {high_score}", True, font_colour)
    screen.blit(hi, (325, 235))

    #draws current score
    score = font.render(f"YOUR SCORE: {current_score}", True, font_colour)
    screen.blit(score, (325, 295))

    # paused title
    paused_font_type = "sfnsmono"
    paused_font_size = 70
    paused_font_bold = True
    paused_font_colour = (0, 240, 60)
    paused_font = pygame.font.SysFont(paused_font_type, paused_font_size, paused_font_bold)
    # draw paused title
    title_top = paused_font.render("GAME OVER", True, paused_font_colour)
    screen.blit(title_top, (265, 125))


    # button font
    button_font = "sfnsmono"
    button_size = 40
    button_bold = False
    button_colour = (255, 255, 255)

    # restart button
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 400, 350, 100), 0, 20)
    restart_font = pygame.font.SysFont(button_font, button_size, button_bold)
    restart_text = restart_font.render("Restart", True, button_colour)
    screen.blit(restart_text, (310, 425))

    # main menu button
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 525, 350, 100), 0, 20)
    main_menu_font = pygame.font.SysFont(button_font, button_size, button_bold)
    main_menu_text = main_menu_font.render("Main Menu", True, button_colour)
    screen.blit(main_menu_text, (290, 550))
    current_score = 0
