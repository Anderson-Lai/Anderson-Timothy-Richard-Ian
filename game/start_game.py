import pygame

def start_game(screen, location, proj_count, proj_time_counter, projectile_x, projectile_y):
    screen.fill((0, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (location + 5, 720, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (600, 0, 200, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 20))
    pygame.draw.rect(screen, (0, 0, 0), (0, 780, 600, 20))
    #projectile timing
    if proj_time_counter % 30 == 0:
        proj_count += 1
    print(proj_time_counter)
    if proj_time_counter % 30 == 0:
        projectile_x.append(location + 5)
        projectile_y.append(720)
    # projectile movement and drawing
    for i in range(len(projectile_y)):
        projectile_y[i] -= 20
        pygame.draw.rect(screen, (0, 255, 0), (projectile_x[i] + 20, projectile_y[i] - 20, 10, 40))
    
