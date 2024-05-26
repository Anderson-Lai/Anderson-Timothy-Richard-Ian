import pygame

def get_score(enemy_kills: int) -> int:
    gain = 10
    score = gain * enemy_kills
    return score

def draw_score(screen, high_score: int, current_score: int):
    font_type = "sfnsmono"
    font_size = 35
    font_bold = False
    font_colour = (0, 0, 0)
    font = pygame.font.SysFont(font_type, font_size, font_bold)

    # draws high score
    hi = font.render(f"HI: {high_score}", True, font_colour)
    screen.blit(hi, (50, 50))

    # draws current score
    score = font.render(f"{current_score}", True, font_colour)
    screen.blit(score, (50, 110))

'''
EXAMPLE VARIABLES
enemy_kills = 4
player_score = score(enemy_kills)
'''

# draw_score(player_score)
