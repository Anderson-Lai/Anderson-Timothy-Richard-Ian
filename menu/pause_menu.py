import pygame

# bg colour, ship colour, permanent upgrades

def generate_pause_menu(screen) -> None:
    screen.fill((0, 0, 0))

    # paused title
    paused_font_type = "sfnsmono"
    paused_font_size = 70
    paused_font_bold = True
    paused_font_colour = (0, 240, 60)
    paused_font = pygame.font.SysFont(paused_font_type, paused_font_size, paused_font_bold)
    # draw paused title
    title_top = paused_font.render("PAUSED", True, paused_font_colour)
    screen.blit(title_top, (265, 125))


    # button font
    button_font = "sfnsmono"
    button_size = 40
    button_bold = False
    button_colour = (255, 255, 255)

    # resume game button
    pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(225, 275, 350, 100), 0, 20)
    resume_font = pygame.font.SysFont(button_font, button_size, button_bold)
    resume_text = resume_font.render("Resume", True, button_colour)
    screen.blit(resume_text, (320, 300))

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