import pygame
from modifications.getting.get_upgrade_state import get_upgrade_state
# money imports
from modifications.getting.get_coins import get_coins
from game.draw_money import draw_money

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
    
    green = (0, 255, 0)
    red = (255, 0, 0)

    first_rect_x = 210 # position of the top of the first rectangle
    space = 90 # pixels from top of rectangle to next rect
    text_difference = 15 # space from top of rect to where text is displayed

    # grey rectangle
    pygame.draw.rect(screen, (69, 69, 69), pygame.Rect(212.5, 60, 550, 700), 0, 40)

    # draws amount of money
    coins = get_coins()
    draw_money(screen, coins, (412.5, 100), 50)
    
    # double shot
    pygame.draw.rect(screen, green if (get_upgrade_state("doubleShot")) else red, pygame.Rect(612.5, first_rect_x, 100, 65))
    double_shot = pygame.font.SysFont(font, font_size)
    rendered_double_shot = double_shot.render("Double shot     $1000", True, text_colour)
    screen.blit(rendered_double_shot, (262.5, first_rect_x + text_difference))

    # multishot
    pygame.draw.rect(screen, green if (get_upgrade_state("multiShot")) else red, pygame.Rect(612.5, first_rect_x + space, 100, 65))
    multi_shot = pygame.font.SysFont(font, font_size)
    rendered_multi_shot = multi_shot.render("Multishot       $1500", True, text_colour)
    screen.blit(rendered_multi_shot, (262.5, first_rect_x + text_difference + space ))

    # extra lives
    pygame.draw.rect(screen, green if (get_upgrade_state("extraLife")) else red, pygame.Rect(612.5, first_rect_x + 2 * space, 100, 65))
    extra_lives = pygame.font.SysFont(font, font_size)
    rendered_extra_lives = extra_lives.render("Extra lives     $2500", True, text_colour)
    screen.blit(rendered_extra_lives, (262.5, first_rect_x + text_difference + 2 * space ))

    # faster fire rate (1)
    pygame.draw.rect(screen, green if (get_upgrade_state("fasterFireRate1")) else red, pygame.Rect(612.5, first_rect_x + 3 * space, 100, 65))
    fire_rate_1 = pygame.font.SysFont(font, font_size)
    rendered_fire_rate_1 = fire_rate_1.render("Fire rate 1     $1500", True, text_colour)
    screen.blit(rendered_fire_rate_1, (262.5, first_rect_x + text_difference + 3 * space ))

    # faster fire rate (2)
    pygame.draw.rect(screen, green if (get_upgrade_state("fasterFireRate2")) else red, pygame.Rect(612.5, first_rect_x + 4 * space, 100, 65))
    fire_rate_2 = pygame.font.SysFont(font, font_size)
    rendered_fire_rate_2 = fire_rate_2.render("Fire rate 2     $3000", True, text_colour)
    screen.blit(rendered_fire_rate_2, (262.5, first_rect_x + text_difference + 4 * space ))

    # faster fire rate (3)
    pygame.draw.rect(screen, green if (get_upgrade_state("fasterFireRate3")) else red, pygame.Rect(612.5, first_rect_x + 5 * space, 100, 65))
    fire_rate_3 = pygame.font.SysFont(font, font_size)
    rendered_fire_rate_3 = fire_rate_3.render("Fire rate 3    $5000", True, text_colour)
    screen.blit(rendered_fire_rate_3, (262.5, first_rect_x + text_difference + 5 * space ))

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))
    return_icon = pygame.image.load("./gameImages/return_icon.png")
    smaller_return_icon = pygame.transform.scale(return_icon, (110, 110))
    screen.blit(smaller_return_icon, (57.5, 57.5))