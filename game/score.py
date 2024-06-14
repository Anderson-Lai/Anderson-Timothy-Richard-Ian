import pygame

def get_score(enemy_kills: int) -> int:
    gain = 10
    score = gain * enemy_kills

    if score <= 0:
        return 0
    return score

def draw_score(screen, high_score, current_score):
    font_type = "sfnsmono"
    font_size = 30
    font_bold = False
    font_colour = (255, 255, 255)
    font = pygame.font.SysFont(font_type, font_size, font_bold)

    #draws high score
    hi = font.render(f"HI: {high_score}", True, font_colour)
    screen.blit(hi, (625, 35))

    #draws current score
    score = font.render(f"{current_score}", True, font_colour)
    screen.blit(score, (625, 95))