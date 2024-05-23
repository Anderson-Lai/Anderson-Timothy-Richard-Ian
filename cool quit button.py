import pygame
import math
pygame.init()


### SET-UP DISPLAY ###
WIDTH = 750 
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('spaceship game')

#==================================================================#

### GLOBAL VARIABLES ###
FPS = 60

font = pygame.font.SysFont('Arial',40,bold=True)
surf = font.render('Quit', True, 'white')
button = pygame.Rect(200,200,110,60)

#==================================================================#

### GAME LOOP ###
running = True
while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
    

    # DRAWING
    screen.fill((2, 100, 255))
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
        pygame.draw.rect(screen,(180,180,180),button )
    else:
        pygame.draw.rect(screen, (110,110,110),button)
    screen.blit(surf,(button.x +5, button.y+5))

    # GAME STATUS UPDATES


#==================================================================#

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
