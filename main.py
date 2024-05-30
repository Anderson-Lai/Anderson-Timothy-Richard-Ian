import pygame
# event handling imports
from eventHandling.handle_events import handle_events
# menu imports
from menu.generate_menu import generate_menu
# shop imports
from shop.generate_shop import generate_shop
# game settings imports
from gameSettings.game_settings import game_settings
from gameSettings.create_settings import create_settings
from gameSettings.get_difficulty import get_difficulty
# game result imports
from gameResults.save_score import save_score
from gameResults.create_score import create_score
from gameResults.get_high_score import get_high_score
# game imports
from game.start_game import start_game
from game.lives import num_lives
from game.lives import draw_removed_hearts
from game.score import get_score
from game.score import draw_score
# power up imports
from powerUps.create_powerups import create_powerups
# cosmetic imports
from cosmetics.create_cosmetics import create_cosmetics

# GAMESTATES: menu, shop, settings, game, dead

def main() -> int:
    # pygame template
    pygame.init()
    proj_count = 0
    proj_time_counter = 0
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
    create_powerups()
    create_cosmetics()

    # values changed by events
    event_variables = {
        "running": True,
        "gameState": "menu",
        "location": 375,
    }

    projectile_x = []
    projectile_y = []

    running: bool = True
    while running:
        # EVENT HANDLING
        # dictionaries are pass by reference by default
        changed_events = handle_events(event_variables)

        # destructuring the dictionary
        gameState: str = changed_events["gameState"]
        location: int = changed_events["location"]
        running: bool = changed_events["running"]
        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((255, 255, 255))

        if gameState == "menu":
            generate_menu(screen)
            # create a rectangle
            # on click, change the 'gameState' variable
        elif gameState == "shop":
            generate_shop(screen)
        elif gameState == "settings":
            game_settings(screen)
        elif gameState == "game":
            # PLACEHOLDER, TESTING VARIABLES
            # score variables
            enemy_kills = 0
            current_score = get_score(enemy_kills)
            high_score = get_high_score()
            difficulty = get_difficulty()
            lives = num_lives(difficulty)

            proj_time_counter += 1
            start_game(screen, location, proj_count, proj_time_counter, projectile_x, projectile_y)
            draw_removed_hearts(screen, lives)
            draw_score(screen, high_score, current_score)

            if lives <= 0:
                event_variables["gameState"] = "dead"
        elif gameState == "dead":
            # get the score on death
            # pass as parameter to this funciton
            # -1 is a placeholder value for now
            save_score(-1)

        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    result: int = main()
    if result != 0:
        print(f"Main exited with error code {result}.")