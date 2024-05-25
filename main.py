import pygame
from generate_menu import generate_menu
from start_game import start_game
from game_settings import game_settings

def main() -> int:
    # pygame template
    pygame.init()
    
    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)

    pygame.key.set_repeat(50, 25)
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    
    gameState: str = "menu"
    location: int = 375
    location_counter: int = 10
    gameDifficulty: int = 0
    sensitivity: int = 10

    running: bool = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # opens settings
                if gameState == "menu" and 650 <= x <= 650 + 100 \
                and 575 <= y <= 575 + 100:
                    gameState = "settings"
                # returns to menu
                elif gameState == "settings" and 50 <= x <= 50 + 125 \
                and 50 <= y <= 50 + 125:
                    gameState = "menu"
                # starts game
                elif gameState == "menu" and 175 <= x <= 175 + 450 \
                and 550 <= y <= 550 + 150:
                    gameState = "game"

                # changing settings
                # changing difficulty
                elif gameState == "settings" and 300 <= x <= 300 + 200 \
                and 200 <= y <= 200 + 100:
                    gameDifficulty += 1
                    if gameDifficulty >= 4:
                        gameDifficulty = 0
                # incrementing sensitivity
                elif gameState == "settings" and 475 <= x <= 525 \
                and 350 <= y <= 350 + 50:
                    sensitivity += 1
                # decrementing sensitivity
                elif gameState == "settings" and 275 <= x <= 325 \
                and 350 <= y <= 350 + 50:
                    sensitivity -= 1
                    if sensitivity <= -1:
                        sensitivity = 0
                
              #spaceship movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and location < 550:
                    location += location_counter
                    print(location)
                elif event.key == pygame.K_LEFT and location > 0:
                    location -= location_counter
                    print(location)
                

        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((0, 0, 0))

        if gameState == "menu":
            generate_menu(screen)
            # create a rectangle
            # on click, chang the 'gameState' variable
        elif gameState == "settings":
            game_settings(screen, gameDifficulty, sensitivity)
        elif gameState == "game":
            start_game(screen, location)
        
        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    result: int = main()
    if result != 0:
        print(f"Main exited with error code {result}.")
