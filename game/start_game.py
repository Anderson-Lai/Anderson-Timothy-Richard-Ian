import pygame
from game.draw_enemies import draw_enemies
from abc import ABC
from modifications.getting.get_upgrade_state import get_upgrade_state

# makes Position an abstract class
class Position(ABC):
    # give a default value for length and width as
    # some inherited classes will not need this, such as the Stars class
    def __init__(self, x: int, y: int, length: int = 0, width: int = 0) -> None:
        self.pos_x = x
        self.pos_y = y
        self.length = length
        self.width = width
    
# down here to avoid a circular import between draw_stars and Position
from game.draw_stars import draw_stars

class Enemy(Position):
    # put in default values for spawntick and type for now
    # allows code to compile as they currently have no implementation
    def __init__(self, x: int, y: int, length: int, width: int, spawntick: int = 0, type: str = "") -> None:
        super().__init__(x, y, length, width)

        #spawntick is the frame the enemy spawned on (for reference on whether or not it will shoot)
        #type is the type of enemy (because we have more than one type)
        self.spawntick = spawntick
        self.type = type
    
    def collide_with_player(self, player_location: int, player_width: int, player_y: int) -> bool:
        if (player_location <= self.pos_x <= player_location + player_width 
            or player_location <= self.pos_x + self.width <= player_location + player_width) \
        and (player_y <= self.pos_y + self.width <= player_y + player_width):
            return True
        return False

class Projectile(Position):
    def __init__(self, x: int, y: int, length: int, width: int) -> None:
        super().__init__(x, y, length, width)

    def pre_collide(self, enemy: Enemy) -> bool:
        if enemy.pos_x <= self.pos_x <= enemy.pos_x + enemy.length \
        and enemy.pos_y <= self.pos_y <= enemy.pos_y + enemy.width:
            return True
        return False

    def post_collide(self, enemy: Enemy) -> bool:
        if enemy.pos_x <= self.pos_x + self.length <= enemy.pos_x + enemy.length \
        and enemy.pos_y <= self.pos_y <= enemy.pos_y + enemy.width:
            return True 
        return False
    

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

# all the projectiles and enemies currently alive

def start_game(screen, location: int, proj_time_counter: int, proj_fire_rate: int, 
proj_speed: int, projectiles: list[Projectile], enemies: list[Enemy], enemy_kills: int) -> int:
    
    screen.fill((0, 5, 40))
    hit = False

    # stars script (create list, spawn stars, etc.)
    draw_stars(screen, proj_time_counter)
    
    # ENEMY TYPES: "glider", "light warship"(small), "heavy warship"(big), "starship"(very big)

    # check if projectile hits enemy
    for i in range(len(projectiles) - 1, -1, -1):
        projectile = projectiles[i]
        for j in range(len(enemies) - 1, -1, -1):
            enemy = enemies[j]
            if projectile.pos_x >= enemy.pos_x:
                if projectile.pre_collide(enemy):
                    del projectiles[i]
                    del enemies[j]
                    enemy_kills += 1
            else:
                if projectile.post_collide(enemy):
                    del projectiles[i]
                    del enemies[j]
                    enemy_kills += 1

    # check if player touches enemy
    for i in range(len(enemies) - 1, -1, -1):
        enemy = enemies[i]
        player_width = 50
        player_y = 720
        if enemy.collide_with_player(location, player_width, player_y):
            del enemies[i]

            # punishments for being hit
            enemy_kills -= 1
            hit = True

    # draw and move projectiles
    for i in range(len(projectiles) - 1, -1, -1):
        pygame.draw.rect(screen, (255, 0, 0), (projectiles[i].pos_x, projectiles[i].pos_y, projectiles[i].length, projectiles[i].width))
        projectiles[i].pos_y -= proj_speed

    # draws and move enemy
    for i in range(len(enemies) - 1, -1, -1):
        pygame.draw.rect(screen, (0, 255, 0), (enemies[i].pos_x, enemies[i].pos_y, enemies[i].length, enemies[i].width))
        enemies[i].pos_y += 10

    # add projectiles
    if proj_time_counter % proj_fire_rate == 0:
        if get_upgrade_state("multiShot"):
            projectiles.append(Projectile(location + 20, 720, 10, 40))
            projectiles.append(Projectile(location + 35, 720, 10, 40))
            projectiles.append(Projectile(location + 5, 720, 10, 40))
        else:
            projectiles.append(Projectile(location + 20, 720, 10, 40))
    
    if proj_time_counter % proj_fire_rate == 10 and get_upgrade_state("doubleShot"):
        if get_upgrade_state("multiShot"):
            projectiles.append(Projectile(location + 20, 720,10, 40))
            projectiles.append(Projectile(location + 35, 720, 10, 40))
            projectiles.append(Projectile(location + 5, 720, 10, 40))
        else:
            projectiles.append(Projectile(location + 20, 720, 10, 40))

    # add an enemy
    if proj_time_counter % 40 == 0:
        enemies.append(Enemy(320, 0, 50, 100))


    # draws player     
    pygame.draw.rect(screen, (0, 255, 0), (location, 720, 50, 50))
    # draws black border
    pygame.draw.rect(screen, (0, 0, 0), (600, 0, 200, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 20, 800))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 20))
    pygame.draw.rect(screen, (0, 0, 0), (0, 780, 600, 20))

    # draws pause button
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(710, 705, 80, 80))
    pause_button = pygame.image.load("./gameImages/pause_button.png")
    smaller_pause_button = pygame.transform.scale(pause_button, (50, 50))
    screen.blit(smaller_pause_button, (725, 720))


    return (enemy_kills, hit)