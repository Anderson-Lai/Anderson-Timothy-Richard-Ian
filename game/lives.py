import pygame
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

def num_lives(gameDifficulty: str) -> int:
    easy_lives = 5
    medium_lives = 3
    hard_lives = 2
    impossible_lives = 1
    if gameDifficulty == "easy":
        return easy_lives
    elif gameDifficulty == "normal": # made medium difficulty default difficulty
        return medium_lives
    elif gameDifficulty == "hard":
        return hard_lives
    elif gameDifficulty == "impossible":
        return impossible_lives

def draw_removed_hearts(screen, lives:int) -> int:
    heart_colour = (255, 0, 0)
    heart_radius = 13
    for i in range(lives):
        pygame.draw.circle(screen, heart_colour, ((625+(heart_radius/2))+heart_radius*2.65*i, 175), heart_radius)


'''
EXAMPLE VARIABLES
game_difficulty = "easy"
lives = num_lives(game_difficulty)
hit = True
'''

# drawremove_hearts(lives, hit)
