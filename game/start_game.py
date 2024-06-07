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

class Moving:
    def __init__(self, x: int, y: int) -> None:
        self.pos_x = x
        self.pos_y = y

class Enemy(Moving):
    pass

class Projectile(Moving):
    def collides_with(self, enemy: Enemy) -> bool:
        if (enemy.pos_x <= self.pos_x <= enemy.pos_x + 50 or enemy.pos_x <= self.pos_x + 25 <= enemy.pos_x + 50) \
        and self.pos_y <= enemy.pos_y + 50:
            return True
        return False

projectiles: list[Projectile] = []
enemies: list[Enemy] = []

def start_game(screen, location, proj_time_counter, proj_fire_rate, proj_speed):
    
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
        
    # add a new bullet
    if proj_time_counter % proj_fire_rate == 0:
        projectiles.append(Projectile(location, 720))

    # projectile movement and drawing
    for i in range(len(projectiles) - 1, -1, -1):
        projectiles[i].pos_y -= proj_speed

        pygame.draw.rect(screen, (255, 0, 0), (projectiles[i].pos_x + 25, projectiles[i].pos_y - 20, 10, 40))
        if projectiles[i].pos_y <= -20: 
            projectiles.pop(i)

    # add an enemy
    if proj_time_counter % 60 == 0:
        # temporary hard-coded values
        enemies.append(Enemy(300, -40))

    # move enemy down
    for i in range(len(enemies)):
        enemies[i].pos_y += 1
    
    # draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), (enemy.pos_x, enemy.pos_y, 50, 50))
        
    # size of projectile:
    # x is 25; y is 20
    # size of enemies:
    # 50, 50
    for i in range(len(projectiles) - 1, -1, -1):
        for j in range(len(enemies) - 1, -1, -1):
            if projectiles[i].collides_with(enemies[j]):
                projectiles.pop(i)
                enemies.pop(j)
                print("something popped")

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

