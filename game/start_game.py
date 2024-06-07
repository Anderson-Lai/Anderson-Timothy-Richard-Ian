import pygame
from game.draw_enemies import draw_enemies
from abc import ABC, abstractmethod


# notes for enemy waves: 
# constant spawning, locked to frame #
# each wave is structured as a list within another list
# [frame # before spawning wave, quantity of enemy 1, quantity of enemy 2, quantity of enemy 3, etc.]
# makes them far easier to manage and run with minimal performance issue
# spawned in random order at a constant rate, up until next wave is spawned
# i will probably make a reference sheet for the enemies (leo yang, eric zheng, etc.)



enemies = []
waves = [
    
    [300, 4, 3]
         

]

# makes Position an abstract class
class Position(ABC):
    @abstractmethod
    def __init__(self, x: int, y: int) -> None:
        self.pos_x = x
        self.pos_y = y

class Enemy(Position):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

class Projectile(Position):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def pre_collide(self, enemy: Enemy) -> bool:
        if enemy.pos_x <= self.pos_x <= enemy.pos_x + 50 \
        and enemy.pos_y <= self.pos_y <= enemy.pos_y + 50:
            return True
        return False

    def post_collide(self, enemy: Enemy) -> bool:
        if enemy.pos_x <= self.pos_x + 10 <= enemy.pos_x + 50 \
        and enemy.pos_y <= self.pos_y <= enemy.pos_y + 50:
            return True 
        return False

projectiles: list[Projectile] = []
enemies: list[Enemy] = []

def start_game(screen, location, proj_time_counter, proj_fire_rate, proj_speed) -> None:
    
    screen.fill((0, 5, 40))

    # down here to avoid a circular import with the Position class
    from game.draw_stars import draw_stars
    # stars script (create list, spawn stars, etc.)
    draw_stars(screen, proj_time_counter)
    
    # ENEMY TYPES: "glider", "light warship"(small), "heavy warship"(big), "starship"(very big)
        
    # add a new projectile
    if proj_time_counter % proj_fire_rate == 0:
        projectiles.append(Projectile(location + 25, 720))

    # draws and moves every projectile
    for i in range(len(projectiles) - 1, -1, -1):
        projectiles[i].pos_y -= proj_speed

        pygame.draw.rect(screen, (255, 0, 0), (projectiles[i].pos_x, projectiles[i].pos_y - 20, 10, 40))
        if projectiles[i].pos_y <= -20: 
            projectiles.pop(i)

    # adds an enemy
    if proj_time_counter % 60 == 0:
        # temporary hard-coded values
        enemies.append(Enemy(300, -40))

    # draws and moves enemy
    for i in range(len(enemies)):
        pygame.draw.rect(screen, (0, 255, 0), (enemies[i].pos_x, enemies[i].pos_y, 50, 50))
        enemies[i].pos_y += 1
    
        
    # size of projectile:
    # x is 10; y is 20
    # size of enemies:
    # 50, 50
    # hit detection
    for i in range(len(projectiles) - 1, -1, -1):
        proj = projectiles[i]
        for j in range(len(enemies) - 1, -1, -1):
            en = enemies[j]
            if proj.pos_x >= en.pos_x:
                if proj.pre_collide(en):
                    del projectiles[i]
                    del enemies[j]
            else:
                if proj.post_collide(en):
                    del projectiles[i]
                    del enemies[j]

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