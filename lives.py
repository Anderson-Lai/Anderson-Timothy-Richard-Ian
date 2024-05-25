def numLives(gameDifficulty:str) -> int:
    easyLives = 5
    mediumLives = 3
    hardLives = 1
    if gameDifficulty == "easy":
        return easyLives
    elif gameDifficulty == "medium":
        return mediumLives
    elif gameDifficulty == "hard":
        return hardLives

def draw_removeHearts(lives:int, hit:bool):
    heartColour = (255, 0, 0)
    heartRadius = 20
    if hit == True:
        lives -= 1
    for i in range(lives):
        pygame.draw.circle(screen, heartColour, ((WIDTH-heartRadius*2.5)-(heartRadius*3)*i, heartRadius*2.5), heartRadius)


'''
These are the variables that make the functions run
gameDifficulty = "easy"
lives = numHearts(gameDifficulty)
hit = True
'''

# this should go under GAME UPDATES. draw_removeHearts(lives, hit)
