import pygame
from draw_text import draw_text
from gameSettings.getting.get_sensitivity import get_sensitivity
from gameSettings.getting.get_difficulty import get_difficulty

def game_settings(screen) -> None:
    screen.fill((0, 0, 0))
    
    difficulty = get_difficulty()

    # to highlight which difficulty is selected
    black = (0, 0, 0)
    orange = (255, 100, 0)

    easy_colour = black
    normal_colour = black
    hard_colour = black

    if difficulty == "easy":
        easy_colour = orange
    elif difficulty == "normal":
        normal_colour = orange
    elif difficulty == "hard":
        hard_colour = orange

                            # DIFFICULTY #
    # difficulty header
    draw_text(screen, "Difficulty", "sfnsmono", 50, (255, 255, 255), True, (245, 212.5))

    # easy difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(75, 312.5, 200, 100))
    draw_text(screen, "Easy", "sfnsmono", 40, easy_colour, False, (125, 337.5))

    # normal difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 312.5, 200, 100))
    draw_text(screen, "Normal", "sfnsmono", 40, normal_colour, False, (325, 337.5))

    # hard difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(525, 312.5, 200, 100))
    draw_text(screen, "Hard", "sfnsmono", 40, hard_colour, False, (575, 337.5))


                            # SENSITIVITY #
    current_sens = get_sensitivity()
    # sensitivity header
    draw_text(screen, "Sensitivity", "sfnsmono", 50, (255, 255, 255), True, (230, 500))

    # current sensitivity
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(350, 600, 100, 50))
    draw_text(screen, f"{current_sens}", "sfnsmono", 40, (0, 0, 0), False, (377.5, 600))

    # increment sensitivity
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(475, 600, 50, 50))
    draw_text(screen, "+", "sfnsmono", 40, (0, 0, 0), False, (488, 598))

    # decrement sensitivity
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, 600, 50, 50))
    draw_text(screen, "+", "sfnsmono", 40, (0, 0, 0), False, (288, 600))


    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))
    return_icon = pygame.image.load("./gameImages/return_icon.png")
    smaller_return_icon = pygame.transform.scale(return_icon, (110, 110))
    screen.blit(smaller_return_icon, (57.5, 57.5))