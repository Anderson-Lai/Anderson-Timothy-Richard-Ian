def numHearts(gameDifficulty:str) -> int:
    hardLives = 1
    mediumLives = 3
    easyLives = 5
    if gameDifficulty == "easy":
        lives = easyLives
    elif gameDifficulty == "medium":
        lives = mediumLives
    elif gameDifficulty == "hard":
        lives = hardLives
    return lives

def draw_removeHearts(hearts:int, hit:bool):
    heartColour = (255, 0, 0)
    heartRadius = 20
    if hit == True:
        hearts -= 1
    for i in range(hearts):
        pygame.draw.circle(screen, heartColour, ((WIDTH-heartRadius*2.5)-(heartRadius*3)*i, heartRadius*2.5), heartRadius)


'''
These are the variables that make the functions run
gameDifficulty = "easy"
hearts = numHearts(gameDifficulty)
hit = True
'''

# this should go under GAME UPDATES. draw_removeHearts(hearts, hit)
