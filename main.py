import pygame
from time import sleep
# event handling imports
from eventHandling.handle_events import handle_events
# menu imports
from menu.generate_menu import generate_menu
# shop imports
from shop.generate_shop import generate_shop
# pause menu imports
from menu.pause_menu import generate_pause_menu
# game settings imports
from gameSettings.game_settings import game_settings
from gameSettings.create_settings import create_settings
from gameSettings.getting.get_difficulty import get_difficulty
# game result imports
from gameResults.save_score import save_score
from gameResults.create_score import create_score
from gameResults.getting.get_high_score import get_high_score
# game imports
from game.start_game import start_game, Enemy, Projectile
from game.lives import num_lives, draw_removed_hearts
from game.score import get_score, draw_score
from game.money import get_money, draw_money
# modification imports (contains cosmetics, powerups, and a currency)
from modifications.create_modifications import create_modifications
from modifications.changing.change_coins import change_coins
# game_states: menu, shop, settings, game, dead
 
def main() -> int:
    pygame.init()
    # pygame window name
    pygame.display.set_caption('Space Invaders')

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

    proj_time_counter: int = 0
    proj_fire_rate: int = 30
    proj_speed: int = 20
    enemy_kills: int = 0
    previous_kills: int = enemy_kills
    projectiles: list[Projectile] = []
    enemies: list[Enemy] = []
    difficulty = get_difficulty()
    lives: int = num_lives(difficulty)
    
    running: bool = True
    while running:
        # EVENT HANDLING
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
            # lives variables
            lives = num_lives(difficulty)
            # money variables
            money = get_money(enemy_kills)

            # checks if any enemies were killed 
            previous_kills = enemy_kills

            proj_time_counter += 1
            # draw the game
            (enemy_kills, hit) = start_game(screen, location, proj_time_counter, proj_fire_rate, proj_speed, projectiles, enemies, enemy_kills)
            draw_removed_hearts(screen, lives)
            draw_score(screen, high_score, current_score)
            
            if hit:
                lives -= 1

            if previous_kills != enemy_kills:
                difference = enemy_kills -  previous_kills
                change_coins(difference * 10)

            if lives <= 0:
                event_variables["gameState"] = "dead"
            if restart:
                save_score(current_score)

                # delete all projectiles and enemies since the game is restarting
                projectiles.clear()
                enemies.clear()

                # reset kills and scores
                enemy_kills = 0
                current_score = 0
                previous_kills = 0

                # break out of the if statement for the next iteration
                event_variables["restart"] = False

                # give the program time to reset everything
                sleep(0.05)
        elif game_state == "dead":
            # get the score on death
            # pass as parameter to this funciton
            save_score(current_score)

        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    result: int = main()
    if result != 0:
        print(f"Main exited with error code {result}.")