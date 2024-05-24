import pygame
from generate_menu import generate_menu
from start_game import start_game
from game_settings import game_settings

def main():
    # pygame template
    pygame.init()
    
    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    
    gameState = "menu"

    running = True
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    location -= 1
     
                elif event.key == pygame.K_RIGHT:
                    location += 1

        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((0, 0, 0))

        if gameState == "menu":
            generate_menu(screen)
            # create a rectangle
            # on click, set menu to false
            # then the game will start
        elif gameState == "settings":
            game_settings(screen)
        elif gameState == "game":
            start_game(screen)
        
        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    main()
