import pygame
from menu import generate_menu

def main():
    
    # pygame template
    pygame.init()
    
    WIDTH = 750
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    
        # GAME STATE UPDATES
        # All game math and comparisons happen here
    
        # DRAWING
        generate_menu(screen)
        
        
        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
        #---------------------------
    
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    main()