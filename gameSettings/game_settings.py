import pygame
from gameSettings.getting.get_sensitivity import get_sensitivity
from gameSettings.getting.get_difficulty import get_difficulty

def game_settings(screen):
    screen.fill((0, 0, 0))
    # header font (provides context for buttons)
    header_font = "sfnsmono"
    header_size = 50
    header_bold = True
    header_colour = (255, 255, 255) # white
    # button font
    button_font = "sfnsmono"
    button_size = 40
    button_bold = False
    button_colour = (0, 0, 0) # black
    
    # to display which difficulty button is selected
    easy_colour = button_colour
    normal_colour = button_colour
    hard_colour = button_colour
    clicked_colour = (255, 100, 0)

    difficulty = get_difficulty()

    if difficulty == "easy":
        easy_colour = clicked_colour
    elif difficulty == "normal":
        normal_colour = clicked_colour
    elif difficulty == "hard":
        hard_colour = clicked_colour

                            # DIFFICULTY #
    # difficulty header
    difficulty_font = pygame.font.SysFont(header_font, header_size, header_bold)
    difficulty_text = difficulty_font.render("Difficulty", True, header_colour)
    screen.blit(difficulty_text, (245, 212.5))
    # easy difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(75, 312.5, 200, 100))
    easy_font = pygame.font.SysFont(button_font, button_size, button_bold)
    easy_text = easy_font.render("Easy", True, easy_colour)
    screen.blit(easy_text, (125, 337.5))
    # normal difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 312.5, 200, 100))
    normal_font = pygame.font.SysFont(button_font, button_size, button_bold)
    normal_text = normal_font.render("Normal", True, normal_colour)
    screen.blit(normal_text, (325, 337.5))
    # hard difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(525, 312.5, 200, 100))
    hard_font = pygame.font.SysFont(button_font, button_size, button_bold)
    hard_text = hard_font.render("Hard", True, hard_colour)
    screen.blit(hard_text, (575, 337.5))

                            # SENSITIVITY #
    current_sens = get_sensitivity()
    # sensitivity header
    sensitivity_font = pygame.font.SysFont(header_font, header_size, header_bold)
    sensitivity_text = sensitivity_font.render("Sensitivity", True, header_colour)
    screen.blit(sensitivity_text, (230, 500))
    # current sensitivity
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(350, 600, 100, 50))
    currentsens_font = pygame.font.SysFont(button_font, button_size, button_bold)
    currentsens_text = currentsens_font.render(f"{current_sens}", True, button_colour)
    screen.blit(currentsens_text, (377.5, 600))
    # increment sensitivity
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(475, 600, 50, 50))
    plus_font = pygame.font.SysFont(button_font, button_size, button_bold)
    plus_text = plus_font.render("+", True, button_colour)
    screen.blit(plus_text, (488, 598))
    # decrement sensitivity
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, 600, 50, 50))
    minus_font = pygame.font.SysFont(button_font, button_size, button_bold)
    minus_text = minus_font.render("-", True, button_colour)
    screen.blit(minus_text, (288, 600))

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))
    return_icon = pygame.image.load("./gameImages/return_icon.png")
    smaller_return_icon = pygame.transform.scale(return_icon, (110, 110))
    screen.blit(smaller_return_icon, (57.5, 57.5))