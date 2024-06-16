import pygame
from game.draw_enemies import draw_enemies
from abc import ABC
from modifications.getting.get_upgrade_state import get_upgrade_state
import random
from math import ceil

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
    def __init__(self, x: int, y: int, length: int, width: int, health: int, spawntick: int = 0) -> None:
        super().__init__(x, y, length, width)

        #spawntick is the frame the enemy spawned on (for reference on whether or not it will shoot)
        self.spawntick = spawntick
        self.health = health
    
    def collide_with_player(self, player_location: int, player_width: int, player_y: int) -> bool:
        if (player_location <= self.pos_x <= player_location + player_width 
            or player_location <= self.pos_x + self.width <= player_location + player_width) \
        and (player_y <= self.pos_y <= player_y + player_width 
             or player_y <= self.pos_y + self.width <= player_y + player_width):
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

class EnemyWaves:
    def __init__(self, wave_frame: int, light_warship_count: int, heavy_warship_count: int, starship_count: int):
        self.wave_frame = wave_frame
        self.light_warship_count = light_warship_count
        self.heavy_warship_count = heavy_warship_count
        self.starship_count = starship_count

        # not found in the constructor
        self.total_enemies = light_warship_count + heavy_warship_count + starship_count

# notes for enemy waves: 
# constant spawning, locked to frame #
# each wave is structured as a list within another list
# [frame # before spawning wave, quantity of enemy 1, quantity of enemy 2, quantity of enemy 3, etc.]
# makes them far easier to manage and run with minimal performance issue
# spawned in random order at a constant rate, up until next wave is spawned
# i will probably make a reference sheet for the enemies (leo yang, eric zheng, etc.)

enemy_types: dict[str, Enemy] = {
    
    "small_ship" : Enemy(0, 0, 20, 20, 1),
    "medium_ship" : Enemy(0, 0, 30, 30, 4),
    "big_ship" : Enemy(0, 0, 40, 40, 30)
}

waves: list[EnemyWaves] = [

    EnemyWaves(0, 3, 3, 3),
    EnemyWaves(100, 0, 0, 0),
    
]

"""
spawn_rate is calculated by :

take the wave_frame difference between wave x and wave x + 1
take the number of enemies wave x has
divide; thus the spawn_rate can be summarized as :

ceil ( ((wave_x+1).wave_frame - (wave_x).wave_frame) / wave_x.total_enemies )

ceiling to prevent any rounding bugs, too fast of a spawn rate > too slow of a spawn rate
"""
spawn_rates: list[int] = []

for i in range(len(waves) - 1):
    frame_difference: int = waves[i + 1].wave_frame - waves[i].wave_frame
    spawn_interval = ceil(frame_difference / waves[i].total_enemies)

    spawn_rates.append(spawn_interval)

    # duplicate the previous spawning rate for the final wave as there is no other wave to base the speed off of
    if i == len(waves) - 2:
        spawn_rates.append(spawn_interval)


curr_spawn_rate_index = 0

def start_game(screen, location: int, proj_time_counter: int, proj_fire_rate: int, 
proj_speed: int, projectiles: list[Projectile], enemies: list[Enemy], enemy_kills: int) -> int:
    
    screen.fill((0, 5, 40))
    hit = False

    spawn_rate = spawn_rates[curr_spawn_rate_index]

    

    # stars script (create list, spawn stars, etc.)
    draw_stars(screen, proj_time_counter)
    

    # draws projectiles
    for i in range(len(projectiles) - 1, -1, -1):
        pygame.draw.rect(screen, (255, 0, 0), (projectiles[i].pos_x, projectiles[i].pos_y, projectiles[i].length, projectiles[i].width))

    # draws enemies
    for i in range(len(enemies) - 1, -1, -1):
        pygame.draw.rect(screen, (0, 255, 0), (enemies[i].pos_x, enemies[i].pos_y, enemies[i].length, enemies[i].width))

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

    # projectile movement
    for i in range(len(projectiles) - 1, -1, -1):
        projectiles[i].pos_y -= proj_speed
    
    # enemy movement
    for i in range(len(enemies) - 1, -1, -1):
        enemies[i].pos_y += 10
    
    # snap the projectile to the enemy's base if projectile would hit the enemy after incrementation
    # prevents bullet from being drawn inside the enemy
    for i in range(len(projectiles) - 1, -1, -1):
        projectile = projectiles[i]
        for j in range(len(enemies) - 1, -1, -1):
            enemy = enemies[j]
            if projectile.pos_x >= enemy.pos_x:
                if projectile.pre_collide(enemy):
                    projectiles[i].pos_y = enemy.pos_y + enemy.width
            else:
                if projectile.post_collide(enemy):
                    projectiles[i].pos_y = enemy.pos_y + enemy.width
    
    if get_upgrade_state("fasterFireRate3"):
        proj_fire_rate = 10
    elif get_upgrade_state("fasterFireRate2"):
        proj_fire_rate = 20
    elif get_upgrade_state("fasterFireRate1"):
        proj_fire_rate = 30

    # add projectiles
    if proj_time_counter % proj_fire_rate == 0:
        if get_upgrade_state("multiShot"):
            projectiles.append(Projectile(location + 20, 720, 10, 40))
            projectiles.append(Projectile(location + 35, 720, 10, 40))
            projectiles.append(Projectile(location + 5, 720, 10, 40))
        else:
            projectiles.append(Projectile(location + 20, 720, 10, 40))
    
    if proj_time_counter % proj_fire_rate == 5 and get_upgrade_state("doubleShot"):
        if get_upgrade_state("multiShot"):
            projectiles.append(Projectile(location + 20, 720,10, 40))
            projectiles.append(Projectile(location + 35, 720, 10, 40))
            projectiles.append(Projectile(location + 5, 720, 10, 40))
        else:
            projectiles.append(Projectile(location + 20, 720, 10, 40))

    # enemy spawning
    if proj_time_counter % spawn_rate == 0:
        curr_enemy_wave = waves[curr_spawn_rate_index]

        # smallest ships
        if curr_enemy_wave.light_warship_count > 0:
            stats = enemy_types["small_ship"]
            enemies.append(Enemy(random.randint(30,570), -40, stats.length, stats.width, stats.health))
            curr_enemy_wave.light_warship_count -= 1
        # medium
        elif curr_enemy_wave.heavy_warship_count > 0:
            stats = enemy_types["medium_ship"]
            enemies.append(Enemy(random.randint(30,570), -40, stats.length, stats.width, stats.health))
            curr_enemy_wave.heavy_warship_count -= 1
        # largest
        elif curr_enemy_wave.starship_count > 0:
            stats = enemy_types["big_ship"]
            enemies.append(Enemy(random.randint(30,570), -40, stats.length, stats.width, stats.health))
            curr_enemy_wave.starship_count -= 1
        # if all the enemies of that wave are exhausted, delete that wave
        else:
            del waves[curr_spawn_rate_index]
            del spawn_rates[curr_spawn_rate_index]

            # both should hit 0 at the same time
            if len(waves) == 0 or len(spawn_rates) == 0:
                pass
                # change the game state

            
    print(enemies, proj_time_counter, spawn_rate)

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

    return (enemy_kills, hit, proj_fire_rate)