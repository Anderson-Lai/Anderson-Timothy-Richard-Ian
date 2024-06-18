import pygame
from time import sleep
from math import ceil
from copy import deepcopy
# event handling imports
from eventHandling.handle_events import handle_events
# menu import
from menu.generate_menu import generate_menu
# shop imports
from shop.generate_shop import generate_shop
# pause menu imports
from menu.pause_menu import generate_pause_menu
# game settings import
from gameSettings.game_settings import game_settings
from gameSettings.create_settings import create_settings
from gameSettings.getting.get_difficulty import get_difficulty
# game result imports
from gameResults.save_score import save_score
from gameResults.create_score import create_score
from gameResults.getting.get_high_score import get_high_score
# game imports
from game.start_game import start_game, Enemy, Projectile, EnemyWaves
from game.lives import num_lives, draw_removed_hearts
from game.score import get_score, draw_score
from game.draw_money import draw_money
from game.reset_game import reset_game
# modification imports (contains cosmetics, powerups, and a currency)
from modifications.create_modifications import create_modifications
from modifications.changing.change_coins import change_coins
from modifications.getting.get_coins import get_coins
# game dead import
from menu.death_menu import death_menu
from menu.win_menu import win_menu
# game_states: menu, shop, settings, game, dead
 
def main() -> int:
    pygame.init()
    # pygame window name
    pygame.display.set_caption("Space Colonizers")

    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 25)

    # create json files to store settings and progress
    create_settings()
    create_score()
    create_modifications()

    # values changed by events
    event_variables = {
        "running": True,
        "gameState": "menu",
        "location": 375,
        "restart": False,
    }

    # became the frame rate variable
    frame_counter: int = 0

    # will be modified by the fasterFireRate upgrade
    proj_fire_rate: int = 40
    # how fast the projectile moves
    proj_speed: int = 20

    enemy_kills: int = 0
    # used to keep track of new kills
    previous_kills: int = enemy_kills

    # all the projectiles and enemies currently drawn
    projectiles: list[Projectile] = []
    enemies: list[Enemy] = []

    # number of each enemy type per wave
    waves: list[EnemyWaves] = [
        EnemyWaves(100, 1, 0, 0),
        EnemyWaves(100, 1, 0, 0),
    ]

    """
    spawn_rate is calculated by :

    take the frame_time of wave x
    take the total number of enemies wave x has
    divide; thus the spawn_rate can be summarized as :

    ceil ( wave_x.frame_time / wave_x.total_enemies )

    ceiling to prevent any rounding bugs, too fast of a spawn rate > too slow of a spawn rate
    """
    # spawn rates of those enemies
    spawn_rates: list[int] = []

    for i in range(len(waves)):
        frames: int = waves[i].frame_time
        spawn_interval = ceil(frames / waves[i].total_enemies)

        spawn_rates.append(spawn_interval)

    waves_copy: list[EnemyWaves] = deepcopy(waves)
    spawn_rates_copy: list[int] = deepcopy(spawn_rates)

    difficulty: str = get_difficulty()
    lives: int = num_lives(difficulty)

    current_score = 0
    
    running: bool = True
    while running:
        # EVENT HANDLING``
        # dictionaries are pass by reference by default
        handle_events(event_variables)

        # destructuring the dictionary
        running: bool = event_variables["running"]
        game_state: str = event_variables["gameState"]
        location: int = event_variables["location"]
        restart: bool = event_variables["restart"]
        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((255, 255, 255))

        if game_state == "menu":
            generate_menu(screen)
            # create a rectangle
            # on click, change the 'game_state' variable

            # all live-changing states all return to menu before going to game
            difficulty = get_difficulty()
            lives = num_lives(difficulty)
        elif game_state == "shop":
            generate_shop(screen)

        elif game_state == "settings":
            game_settings(screen)

        elif game_state == "paused":
            generate_pause_menu(screen)
        elif game_state == "game":
            # score variables
            current_score = get_score(enemy_kills)
            high_score = get_high_score()
            # difficulty variables
            difficulty = get_difficulty()
            # money variables
            money = get_coins()

            # checks if any enemies were killed 
            previous_kills = enemy_kills

            # draw the game
            (enemy_kills, lives, proj_fire_rate, event_variables["gameState"]) = \
            start_game(screen, location, frame_counter, 
                    proj_fire_rate, proj_speed, projectiles, 
                    enemies, enemy_kills, game_state,
                    waves_copy, spawn_rates_copy, lives)
            draw_removed_hearts(screen, lives)
            draw_score(screen, high_score, current_score)
            draw_money(screen, money, (650, 320), 30)

            frame_counter += 1

            # punishment for getting hit
            if lives <= 0:
                event_variables["gameState"] = "dead"

            # check for any new kills to increase coin amount
            if previous_kills != enemy_kills:
                difference = enemy_kills - previous_kills
                change_coins(difference * 50)

            if restart:
                (enemy_kills, current_score, previous_kills, lives, waves_copy, spawn_rates_copy) = \
                reset_game(current_score, projectiles, enemies, enemy_kills, previous_kills, event_variables,
                        waves_copy, spawn_rates_copy, waves, spawn_rates, difficulty)
        elif game_state == "dead":
            death_menu(screen, high_score, current_score)

            if restart:
                (enemy_kills, current_score, previous_kills, lives, waves_copy, spawn_rates_copy) = \
                reset_game(current_score, projectiles, enemies, enemy_kills, previous_kills, event_variables,
                        waves_copy, spawn_rates_copy, waves, spawn_rates, difficulty)
        elif game_state == "win":
            win_menu(screen, high_score, current_score)

            if restart:
                (enemy_kills, current_score, previous_kills, lives, waves_copy, spawn_rates_copy) = \
                reset_game(current_score, projectiles, enemies, enemy_kills, previous_kills, event_variables,
                        waves_copy, spawn_rates_copy, waves, spawn_rates, difficulty)
            
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    # in case the 'x' is pressed
    save_score(current_score)
    
    return 0

if __name__ == "__main__":
    result: int = main()
    if result != 0:
        print(f"Main exited with error code {result}.")
