import pygame
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

def num_lives(gameDifficulty:int) -> int:
    easy_lives = 5
    medium_lives = 3
    hard_lives = 2
    impossible_lives = 1
    if gameDifficulty == 1:
        return easy_lives
    elif gameDifficulty == 0: # made medium difficulty default difficulty
        return medium_lives
    elif gameDifficulty == 2:
        return hard_lives
    elif gameDifficulty == 3:
        return impossible_lives

def draw_removed_hearts(screen, lives:int, hit:bool):
    heart_colour = (255, 0, 0)
    heart_radius = 20
    if hit == True:
        lives -= 1
    for i in range(lives):
        pygame.draw.circle(screen, heart_colour, ((heart_radius*2.5)+(heart_radius*3)*i, heart_radius*2.5), heart_radius)


'''
EXAMPLE VARIABLES
game_difficulty = "easy"
lives = num_lives(game_difficulty)
hit = True
'''

# drawremove_hearts(lives, hit)
