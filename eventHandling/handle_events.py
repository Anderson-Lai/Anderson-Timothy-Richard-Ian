import pygame
from gameSettings.changing.change_difficulty import change_difficulty
from gameSettings.changing.change_sensitivity import change_sensitivity
from gameSettings.getting.get_sensitivity import get_sensitivity

def handle_events(events: dict) -> dict:

    gameState: str = events["gameState"]
    location: int = events["location"]
    # destructuring events["running"] should not be necessary
    # as it should only be used once in the pygame.QUIT event
    
    sensitivity = get_sensitivity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events["running"] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # opens settings
            if gameState == "menu" and 650 <= x <= 650 + 100 \
            and 575 <= y <= 575 + 100:
                events["gameState"] = "settings"
            # starts game
            elif gameState == "menu" and 175 <= x <= 175 + 450 \
            and 550 <= y <= 550 + 150:
                events["gameState"] = "game"
            # open shop
            elif gameState == "menu" and 50 <= x <= 50 + 100 \
            and 575 <= y <= 575 + 100:
                events["gameState"] = "shop"
            # returns to menu
            elif gameState == "settings" and 50 <= x <= 50 + 125 \
            and 50 <= y <= 50 + 125:
                events["gameState"] = "menu"
            # opens pause screen
            elif gameState == "game" and 710 <= x <= 710 + 80 \
            and 705 <= y <= 705 + 80:
                events["gameState"] = "menu"

            # changing settings
            # changing difficulty
            elif gameState == "settings" and 75 <= x <= 75 + 200 \
            and 312.5 <= y <= 312.5 + 100:
                change_difficulty("easy")
            elif gameState == "settings" and 300 <= x <= 300 + 200 \
            and 312.5 <= y <= 312.5 + 100:
                change_difficulty("normal")
            elif gameState == "settings" and 525 <= x <= 525 + 200 \
            and 312.5 <= y <= 312.5 + 100:
                change_difficulty("hard")
            # incrementing sensitivity
            elif gameState == "settings" and 475 <= x <= 525 \
            and 600 <= y <= 650:
                change_sensitivity(1)
            # decrementing sensitivity
            elif gameState == "settings" and 275 <= x <= 325 \
            and 600 <= y <= 650:
                change_sensitivity(-1)
            
        #spaceship movement
        if event.type == pygame.KEYDOWN:
            # move right
            if event.key == pygame.K_RIGHT and location <= 535:
                events["location"] += sensitivity

                if location + sensitivity >= 535:
                    events["location"] = 535
            # move left
            elif event.key == pygame.K_LEFT and location >= 25:
                events["location"] -= sensitivity
                
                if location - sensitivity <= 25:
                    events["location"] = 25

    return events