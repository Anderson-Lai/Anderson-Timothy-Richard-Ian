import pygame
import random
from game.enemies import draw_enemies

# notes for enemy waves: 
# constant spawning, locked to frame #
# each wave is structured as a list within another list
# [frame # before spawning wave, quantity of enemy 1, quantity of enemy 2, quantity of enemy 3, etc.]
# makes them far easier to manage and run with minimal performance issue
# spawned in random order at a constant rate, up until next wave is spawned
# i will probably make a reference sheet for the enemies (leo yang, eric zheng, etc.)

stars = []
enemies = []

def start_game(screen, location, proj_count, proj_time_counter, projectile_x, projectile_y, proj_fire_rate):
    screen.fill((0, 5, 40))

    #stars script (create list, spawn stars, etc.)
    if proj_time_counter % 4 == 0 :
        stars.append([random.randint(-280, 280), random.randint(-15, 15), 2])
    for n in range(len(stars) - 1, -1, -1):
        
        pygame.draw.rect(screen, (255, 255, 255), (round(stars[n][0]) + 310, round(stars[n][1]), 5, 5))

        if stars[n][1] >= 800: 
            stars.pop(n)
        else: 
            stars[n][1] += 5 * stars[n][2]
            stars[n][2] *= 1.01

    #enemies
    # ENEMY TYPES: "glider", ""
        

    #projectile timing
    if proj_time_counter % proj_fire_rate == 0:
        proj_count += 1
    if proj_time_counter % proj_fire_rate == 0:
        projectile_x.append(location + 5)
        projectile_y.append(720)
    # projectile movement and drawing
    for i in range(len(projectile_y) - 1, -1, -1):
        projectile_y[i] -= 20
        if projectile_y[i] <= -20: 
            projectile_y.pop(i)
            projectile_x.pop(i)

        pygame.draw.rect(screen, (255, 0, 0), (projectile_x[i] + 20, projectile_y[i] - 20, 10, 40))
    
    pygame.draw.rect(screen, (0, 255, 0), (location + 5, 720, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (600, 0, 200, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 20))
    pygame.draw.rect(screen, (0, 0, 0), (0, 780, 600, 20))
