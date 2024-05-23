import pygame
from generate_menu import generate_menu
from start_game import start_game
from game_settings import game_settings

def main():
    
    # pygame template
    pygame.init()
    
    WIDTH = 750
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    
    running = True
    menu = True
    gameSettings = False
    startGame = False

    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if menu: # check for collision when opening game settings
                    menu = False
                    startGame = False
                    gameSettings = True
                elif gameSettings: # check for collision
                    # return to menu
                    gameSettings = False
                    startGame = False
                    menu = True
                elif menu: 
                    # make sure this checks for clicking on "start game button"
                    menu = False
                    gameSettings = False
                    startGame = True
            
    
        # GAME STATE UPDATES
        # All game math and comparisons happen here
    
        # DRAWING
        screen.fill((0, 0, 0))

        if menu:
            generate_menu(screen)
            # create a rectangle
            # on click, set menu to false
            # then the game will start
        elif gameSettings:
            game_settings(screen)
        elif startGame:
            start_game(screen)
        
        
        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
        #---------------------------
    
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    main()