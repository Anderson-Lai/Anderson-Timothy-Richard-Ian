import pygame
from abc import ABC
from modifications.getting.get_upgrade_state import get_upgrade_state
import random

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
    def __init__(self, x: int, y: int, length: int, width: int, health: int, movement_speed: int = 0) -> None:
        super().__init__(x, y, length, width)

        self.movement_speed = movement_speed
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
    def __init__(self, frame_time: int, light_warship_count: int, heavy_warship_count: int, starship_count: int):
        self.frame_time = frame_time
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
    "small_ship" : Enemy(0, 0, 20, 20, 1, 8),
    "medium_ship" : Enemy(0, 0, 30, 30, 4, 4),
    "big_ship" : Enemy(0, 0, 40, 40, 30, 2)
}

def start_game(screen, location: int, frame_counter: int, proj_fire_rate: int, 
proj_speed: int, projectiles: list[Projectile], enemies: list[Enemy], enemy_kills: int, game_state: str,
waves: list[EnemyWaves], spawn_rates: list[int], lives: int) -> tuple[int, bool, int, str]:
    
    screen.fill((0, 5, 40))
    hit = False

    # stars script (create list, spawn stars, etc.)
    draw_stars(screen, frame_counter)
    
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
                    enemies[j].health -= 1
                    if enemies[j].health <= 0:
                        del enemies[j]
                    enemy_kills += 1
            else:
                if projectile.post_collide(enemy):
                    del projectiles[i]
                    enemies[j].health -= 1
                    if enemies[j].health <= 0:
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
            lives -= 1

    # projectile movement
    for i in range(len(projectiles) - 1, -1, -1):
        projectiles[i].pos_y -= proj_speed
    
    # enemy movement
    for i in range(len(enemies) - 1, -1, -1):
        enemies[i].pos_y += enemies[i].movement_speed
        if enemies[i].pos_y >= 800:
            enemies.pop(i)
            lives -= 1

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
    if frame_counter % proj_fire_rate == 0:
        if get_upgrade_state("multiShot"):
            projectiles.append(Projectile(location + 20, 720, 10, 40))
            projectiles.append(Projectile(location + 35, 720, 10, 40))
            projectiles.append(Projectile(location + 5, 720, 10, 40))
        else:
            projectiles.append(Projectile(location + 20, 720, 10, 40))
    
    if frame_counter % proj_fire_rate == 5 and get_upgrade_state("doubleShot"):
        if get_upgrade_state("multiShot"):
            projectiles.append(Projectile(location + 20, 720,10, 40))
            projectiles.append(Projectile(location + 35, 720, 10, 40))
            projectiles.append(Projectile(location + 5, 720, 10, 40))
        else:
            projectiles.append(Projectile(location + 20, 720, 10, 40))

    # enemy spawning

    try:
        spawn_rate = spawn_rates[0]
        if frame_counter % spawn_rate == 0:
            curr_enemy_wave = waves[0]

            # smallest ships
            if curr_enemy_wave.light_warship_count > 0:
                stats = enemy_types["small_ship"]
                enemies.append(Enemy(random.randint(30, 570), -40, stats.length, stats.width, stats.health, stats.movement_speed))
                curr_enemy_wave.light_warship_count -= 1

            # medium
            elif curr_enemy_wave.heavy_warship_count > 0:
                stats = enemy_types["medium_ship"]
                enemies.append(Enemy(random.randint(30, 570), -40, stats.length, stats.width, stats.health, stats.movement_speed))
                curr_enemy_wave.heavy_warship_count -= 1

            # largest
            elif curr_enemy_wave.starship_count > 0:
                stats = enemy_types["big_ship"]
                enemies.append(Enemy(random.randint(30, 570), -40, stats.length, stats.width, stats.health, stats.movement_speed))
                curr_enemy_wave.starship_count -= 1

            # if all the enemies of that wave are exhausted, delete that wave
            else:
                del waves[0]
                del spawn_rates[0]

                # both should hit 0 at the same time
                # checks if the player magically kills all the enemies immediately after the final wave is finished spawning
                if (len(waves) == 0 or len(spawn_rates) == 0) and len(enemies) == 0:
                    game_state = "win"
    except IndexError:
        # checks if all the enemies are killed or not
        if (len(waves) == 0 or len(spawn_rates) == 0) and len(enemies) == 0:
            game_state = "win"

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

    return (enemy_kills, lives, proj_fire_rate, game_state)
