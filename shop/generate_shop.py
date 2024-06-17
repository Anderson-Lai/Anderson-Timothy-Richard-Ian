import pygame
from textDrawing.draw_text import draw_text
from modifications.getting.get_upgrade_state import get_upgrade_state
# money imports
from modifications.getting.get_coins import get_coins
from game.draw_money import draw_money

"""
items:

"doubleShot": False, <- rapidly shooting a second set of bullet after the first
"multiShot": False, <- shooting 3 bullets at the same time
"extraLife": False, <- + 2 lives
"fasterFireRate1": False, <- decrement waiting time
"fasterFireRate2": False,
"fasterFireRate3": False,
"""

def generate_shop(screen) -> None:
    screen.fill((0, 0, 0))

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
    draw_text(screen, "Double shot          $1000", "sfnsmono", 28, (255, 255, 255), False, (262.5, first_rect_x + text_difference))

    # multishot
    pygame.draw.rect(screen, green if (get_upgrade_state("multiShot")) else red, pygame.Rect(612.5, first_rect_x + space, 100, 65))
    draw_text(screen, "Multishot            $1500", "sfnsmono", 28, (255, 255, 255), False, (262.5, first_rect_x + text_difference + space))

    # extra lives
    pygame.draw.rect(screen, green if (get_upgrade_state("extraLife")) else red, pygame.Rect(612.5, first_rect_x + 2 * space, 100, 65))
    draw_text(screen, "Extra lives          $2500", "sfnsmono", 28, (255, 255, 255), False, (262.5, first_rect_x + text_difference + space*2))

    # faster fire rate (1)
    pygame.draw.rect(screen, green if (get_upgrade_state("fasterFireRate1")) else red, pygame.Rect(612.5, first_rect_x + 3 * space, 100, 65))
    draw_text(screen, "Fire rate 1          $1500", "sfnsmono", 28, (255, 255, 255), False, (262.5, first_rect_x + text_difference + space*3))

    # faster fire rate (2)
    pygame.draw.rect(screen, green if (get_upgrade_state("fasterFireRate2")) else red, pygame.Rect(612.5, first_rect_x + 4 * space, 100, 65))
    draw_text(screen, "Fire rate 2          $3000", "sfnsmono", 28, (255, 255, 255), False, (262.5, first_rect_x + text_difference + space*4))

    # faster fire rate (3)
    pygame.draw.rect(screen, green if (get_upgrade_state("fasterFireRate3")) else red, pygame.Rect(612.5, first_rect_x + 5 * space, 100, 65))
    draw_text(screen, "Fire rate 3          $5000", "sfnsmono", 28, (255, 255, 255), False, (262.5, first_rect_x + text_difference + space*5))

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))
    return_icon = pygame.image.load("./gameImages/return_icon.png")
    smaller_return_icon = pygame.transform.scale(return_icon, (110, 110))
    screen.blit(smaller_return_icon, (57.5, 57.5))