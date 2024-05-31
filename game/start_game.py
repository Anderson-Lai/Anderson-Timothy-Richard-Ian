import pygame
import random

stars = []

def start_game(screen, location, proj_count, proj_time_counter, projectile_x, projectile_y, proj_fire_rate):
    screen.fill((0, 5, 40))

    if proj_time_counter % 4 == 0 :
        stars.append([random.randint(-280, 280), random.randint(-15, 15), 2])
    for n in range(len(stars) - 1, -1, -1):
        
        pygame.draw.rect(screen, (255, 255, 255), (round(stars[n][0]) + 310, round(stars[n][1]), 5, 5))

        if stars[n][1] >= 800: 
            stars.pop(n)
        else: 
            stars[n][1] += 5 * stars[n][2]

        
        

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
