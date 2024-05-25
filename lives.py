def num_lives(game_difficulty:str) -> int:
    easy_lives = 5
    medium_lives = 3
    hard_lives = 1
    if game_difficulty == "easy":
        return easy_lives
    elif game_difficulty == "medium":
        return medium_lives
    elif game_difficulty == "hard":
        return hard_lives

def drawremove_hearts(lives:int, hit:bool):
    heart_colour = (255, 0, 0)
    heart_radius = 20
    if hit == True:
        lives -= 1
    for i in range(lives):
        pygame.draw.circle(screen, heart_colour, ((WIDTH-heart_radius*2.5)-(heart_radius*3)*i, heart_radius*2.5), heart_radius)


'''
These are the variables that make the functions run
game_difficulty = "easy"
lives = num_lives(game_difficulty)
hit = True
'''

# this should go under GAME UPDATES. drawremove_hearts(lives, hit)
