import pygame
# event handling imports
from eventHandling.handle_events import handle_events
# menu imports
from menu.generate_menu import generate_menu
# shop imports
from shop.generate_shop import generate_shop
# game settings imports
from gameSettings.game_settings import game_settings
from gameSettings.get_settings import get_settings
from gameSettings.create_settings import create_settings
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

#GAMESTATES: menu, settings, game, dead

def main() -> int:
    # pygame template
    pygame.init()
    proj_count = 0
    proj_time_counter = 0
    # pygame window name
    pygame.display.set_caption('Space Colonizers')

    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 25)

    # create the score.json file
    create_score()
    
    # create the settings.json file
    create_settings()
    settings = get_settings()

    # values changed by events
    mutable_events = {
        "running": True,
        "gameState": "menu",
        "location": 375,
        "difficultyIndex": settings["difficultyIndex"],
        "sensitivity": settings["sensitivity"],
    }

    projectile_x = []
    projectile_y = []

    running: bool = True
    while running:
        # EVENT HANDLING
        # dictionaries are pass by reference by default
        changed_events = handle_events(mutable_events)

        # destructuring the dictionary
        gameState: str = changed_events["gameState"]
        location: int = changed_events["location"]
        difficultyIndex: int = changed_events["difficultyIndex"]
        sensitivity: int = changed_events["sensitivity"]
        running: bool = changed_events["running"]
        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((0, 0, 0))

        if gameState == "menu":
            generate_menu(screen)
            # create a rectangle
            # on click, change the 'gameState' variable
        elif gameState == "settings":
            game_settings(screen, difficultyIndex, sensitivity)
        elif gameState == "game":
            gameStateSettings = get_settings()

            # PLACEHOLDER, TESTING VARIABLES
            # score variables
            enemy_kills = 0
            # if enemyhit() == True:
                # enemy_kills += 1
            current_score = get_score(enemy_kills)
            high_score = get_high_score()
            # lives variables
            lives = num_lives(gameStateSettings["difficulty"])
            # if playerhit() == True:
                # lives -= 1

            proj_time_counter += 1
            start_game(screen, location, proj_count, proj_time_counter, projectile_x, projectile_y)
            draw_removed_hearts(screen, lives)
            draw_score(screen, high_score, current_score)
            if lives <= 0:
                mutable_events["gameState"] = "dead"
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
