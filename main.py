import pygame
from generate_menu import generate_menu
from start_game import start_game

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

    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and menu:
                # add collision checking to check if the click is inside
                # the start game button's bounds

                # this will call start_game()
                menu = False
            
    
        # GAME STATE UPDATES
        # All game math and comparisons happen here
    
        # DRAWING
        screen.fill((0, 0, 0))

        if menu:
            generate_menu(screen)
            # create a rectangle
            # on click, set menu to false
            # then the game will start
        else:
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