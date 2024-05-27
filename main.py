import pygame
# event handling imports
from eventHandling.handle_events import handle_events
# menu imports
from menu.generate_menu import generate_menu
# game settings imports
from gameSettings.game_settings import game_settings
from gameSettings.get_settings import get_settings
from gameSettings.create_settings import create_settings
# game imports
from game.start_game import start_game
from game.lives import num_lives
from game.lives import draw_removed_hearts
from game.score import get_score
from game.score import draw_score

def main() -> int:
    # pygame template
    pygame.init()

    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 25)
    
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
            # on click, chang the 'gameState' variable
        elif gameState == "settings":
            game_settings(screen, difficultyIndex, sensitivity)
        elif gameState == "game":
            # placeholder, testing variables
            # score variables
            enemy_kills = 4
            current_score = get_score(enemy_kills)
            high_score = 170

            # lives variables
            lives = num_lives(mutable_events["difficultyIndex"])
            hit = True
            start_game(screen, location)
            draw_removed_hearts(screen, lives, hit)
            draw_score(screen, high_score, current_score)

        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    result: int = main()
    if result != 0:
        print(f"Main exited with error code {result}.")
