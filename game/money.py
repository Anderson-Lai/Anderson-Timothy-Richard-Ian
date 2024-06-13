import pygame

def get_money(enemy_kills: int) -> int:
    gain = 100
    money = gain * enemy_kills
    return money

def draw_money(screen, money):
    font_type = "comic sans"
    font_size = 30
    font_bold = False
    font_colour = (255, 255, 0)
    font = pygame.font.SysFont(font_type, font_size, font_bold)

    # draws amount of dollar moneys
    score = font.render(f"${money}", True, font_colour)
    screen.blit(score, (650, 310))