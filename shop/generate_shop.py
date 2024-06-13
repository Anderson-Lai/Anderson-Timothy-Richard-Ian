import pygame
from modifications.getting.get_upgrade_state import upgrade_state

"""
items:
ship colour <- do this last

"doubleShot": False, <- rapidly shooting a second set of bullet after the first
"multiShot": False, <- shooting 3 bullets at the same time
"extraLife": False, <- + 2 lives
"fasterFireRate1": False, <- decrement waiting time
"fasterFireRate2": False,
"fasterFireRate3": False,
"""

def generate_shop(screen) -> None:
    screen.fill((0, 0, 0))

    font = "sfnsmono"
    font_size = 28
    text_colour = (255, 255, 255)
    
    green = (0, 235, 0)
    red = (255, 0, 0)

    text_difference = 35 # space from top of rect to where text is displayed
    space = 90 # pixels from top of rectangle to next rect
    first_rect_x = 100 # position of the top of the first rectangle

    state = upgrade_state()
    
    # double shot
    pygame.draw.rect(screen, green, pygame.Rect(450, first_rect_x, 100, 65))
    double_shot = pygame.font.SysFont(font, font_size)
    rendered_double_shot = double_shot.render("Double shot $1000", True, text_colour)
    screen.blit(rendered_double_shot, (200, first_rect_x + text_difference))

    # multishot
    pygame.draw.rect(screen, green, pygame.Rect(450, first_rect_x + space, 100, 65))
    multi_shot = pygame.font.SysFont(font, font_size)
    rendered_multi_shot = multi_shot.render("Multi-shot $1500", True, text_colour)
    screen.blit(rendered_multi_shot, (200, first_rect_x + text_difference + space ))

    # extra lives
    pygame.draw.rect(screen, green, pygame.Rect(450, first_rect_x + 2 * space, 100, 65))
    extra_lives = pygame.font.SysFont(font, font_size)
    rendered_extra_lives = extra_lives.render("Extra-Lives $2500", True, text_colour)
    screen.blit(rendered_extra_lives, (200, first_rect_x + text_difference + 2 * space ))

    # faster fire rate (1)
    pygame.draw.rect(screen, green, pygame.Rect(450, first_rect_x + 3 * space, 100, 65))
    fire_rate_1 = pygame.font.SysFont(font, font_size)
    rendered_fire_rate_1 = fire_rate_1.render("Faster fire rate 1 $1500", True, text_colour)
    screen.blit(rendered_fire_rate_1, (200, first_rect_x + text_difference + 3 * space ))

    # faster fire rate (2)
    pygame.draw.rect(screen, green, pygame.Rect(450, first_rect_x + 4 * space, 100, 65))
    fire_rate_2 = pygame.font.SysFont(font, font_size)
    rendered_fire_rate_2 = fire_rate_2.render("Faster fire rate 2 $3000", True, text_colour)
    screen.blit(rendered_fire_rate_2, (200, first_rect_x + text_difference + 4 * space ))

    # faster fire rate (3)
    pygame.draw.rect(screen, green, pygame.Rect(450, first_rect_x + 5 * space, 100, 65))
    fire_rate_3 = pygame.font.SysFont(font, font_size)
    rendered_fire_rate_3 = fire_rate_3.render("Faster fire rate 3 $5000", True, text_colour)
    screen.blit(rendered_fire_rate_3, (200, first_rect_x + text_difference + 5 * space ))