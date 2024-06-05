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
waves = [
    
    [300, 4, 3]
         

]

def start_game(screen, location, proj_count, proj_time_counter, projectile_x, projectile_y, proj_fire_rate, proj_speed, enemy_y, enemy_x):
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
    # ENEMY TYPES: "glider", "light warship"(small), "heavy warship"(big), "starship"(very big)
        

    #projectile timing
    if proj_time_counter % proj_fire_rate == 0:
        proj_count += 1
    if proj_time_counter % proj_fire_rate == 0:
        projectile_x.append(location + 5)
        projectile_y.append(720)
    # projectile movement and drawing
    for i in range(len(projectile_y) - 1, -1, -1):
        projectile_y[i] -= proj_speed
        if projectile_y[i] <= -proj_speed: 
            projectile_y.pop(i)
            projectile_x.pop(i)

        pygame.draw.rect(screen, (255, 0, 0), (projectile_x[i] + 20, projectile_y[i] - 20, 10, 40))

    
    if proj_time_counter % 60 == 0:
        enemy_y.append(20)
        enemy_x.append(300)
    for w in range(len(enemy_y) -1, -1, -1):
        enemy_y[w] += 1
    for r in range(len(enemy_y) -1, -1, -1):
        for j in range(len(projectile_y) -1, -1, -1):
            if enemy_y[r] >= projectile_y[j] - 20 and enemy_x[r] < projectile_x[j] + 80 and enemy_x[r] + 50 > projectile_x[j] + 70:

                enemy_y.pop(r)
                projectile_y.pop(j)
                projectile_x.pop(j)


    # black border
    pygame.draw.rect(screen, (0, 255, 0), (location + 5, 720, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (600, 0, 200, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 20))
    pygame.draw.rect(screen, (0, 0, 0), (0, 780, 600, 20))

    # pause button
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(710, 705, 80, 80))
    pause_button = pygame.image.load("./gameImages/pause_button.png")
    smaller_pause_button = pygame.transform.scale(pause_button, (50, 50))
    screen.blit(smaller_pause_button, (725, 720))


    for k in range(len(enemy_y) -1, -1, -1):
  
        pygame.draw.rect(screen, (0, 255, 0), (250, enemy_y[k], 50, 50))
