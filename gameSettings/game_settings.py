import pygame

def game_settings(screen):
    screen.fill((0, 0, 0))

    # sensitivy and difficulty buttons
    # difficulty text
    font = "sfnsmono"
    size = 50
    bold = True
    colour = (255, 255, 255)
    difficulty_font = pygame.font.SysFont(font, size, bold)
    # draw difficulty text
    difficulty_text = difficulty_font.render("Difficulty", True, colour)
    screen.blit(difficulty_text, (245, 200))

    # difficulty
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(75, 300, 200, 100))
    easy_font = pygame.font.SysFont(font, 40, False)
    easy_text = easy_font.render("Easy", True, (0, 0, 0))
    screen.blit(easy_text, (125, 325))

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(300, 300, 200, 100))
    normal_font = pygame.font.SysFont(font, 40, False)
    normal_text = normal_font.render("Normal", True, (0, 0, 0))
    screen.blit(normal_text, (325, 325))

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(525, 300, 200, 100))
    hard_font = pygame.font.SysFont(font, 40, False)
    hard_text = hard_font.render("Hard", True, (0, 0, 0))
    screen.blit(hard_text, (575, 325))


    # sensitivity
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(350, 650, 100, 50))
    # increment sensitivity
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(475, 650, 50, 50))
    # decrement sensitivity
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(275, 650, 50, 50))

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))
    return_icon = pygame.image.load("return_icon.png")
    smaller_return_icon = pygame.transform.scale(return_icon, (110, 110))
    screen.blit(smaller_return_icon, (57.5, 57.5))