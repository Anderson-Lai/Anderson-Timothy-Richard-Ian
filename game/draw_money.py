import pygame

def draw_money(screen, money, coordinates, size):
    font_type = "sfnsmono"
    font_size = size
    font_bold = False
    font_colour = (255, 255, 0)
    font = pygame.font.SysFont(font_type, font_size, font_bold)

    # draws amount of dollar moneys
    score = font.render(f"${money}", True, font_colour)
    screen.blit(score, coordinates)