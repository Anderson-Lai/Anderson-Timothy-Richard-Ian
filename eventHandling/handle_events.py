import pygame
from gameSettings.changing.change_difficulty import change_difficulty
from gameSettings.changing.change_sensitivity import change_sensitivity
from gameSettings.getting.get_sensitivity import get_sensitivity
from modifications.getting.get_coins import get_coins
from modifications.changing.change_upgrade import change_upgrade

def handle_events(events: dict):

    game_state: str = events["gameState"]
    location: int = events["location"]
    # destructuring events["running"] should not be necessary
    # as it should only be used once in the pygame.QUIT event

    coins = get_coins()
    sensitivity = get_sensitivity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events["running"] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # opens settings
            if game_state == "menu" and 650 <= x <= 650 + 100 \
            and 575 <= y <= 575 + 100:
                events["gameState"] = "settings"
            # starts game
            elif game_state == "menu" and 175 <= x <= 175 + 450 \
            and 550 <= y <= 550 + 150:
                events["gameState"] = "game"
            # open shop
            elif game_state == "menu" and 50 <= x <= 50 + 100 \
            and 575 <= y <= 575 + 100:
                events["gameState"] = "shop"
            # returns to menu
            elif game_state == "settings" and 50 <= x <= 50 + 125 \
            and 50 <= y <= 50 + 125:
                events["gameState"] = "menu"
            
            # buying items from the shop
            # double shot
            elif game_state == "shop" and 450 <= x <= 450 + 100 \
            and 100 <= y <= 100 + 65:
                if coins >= 1000:
                    change_upgrade("doubleShot", True)
                    
            # multi shot
            elif game_state == "shop" and 450 <= x <= 450 + 100 \
            and 190 <= y <= 190 + 65:
                if coins >= 1500:
                    change_upgrade("multiShot", True)
            # extra life
            elif game_state == "shop" and 450 <= x <= 450 + 100 \
            and 280 <= y <= 280 + 65:
                if coins >= 2500:
                    change_upgrade("extraLife", True)
            # faster fire rate 1
            elif game_state == "shop" and 450 <= x <= 450 + 100 \
            and 370 <= y <= 370 + 65:
                if coins >= 1500:
                    change_upgrade("fasterFireRate1", True)
            # faster fire rate 2
            elif game_state == "shop" and 450 <= x <= 450 + 100 \
            and 460 <= y <= 460 + 65:
                if coins >= 3000:
                    change_upgrade("fasterFireRate2", True)
            # faster fire rate 3
            elif game_state == "shop" and 450 <= x <= 450 + 100 \
            and 550 <= y <= 550 + 65:
                if coins >= 5000:
                    change_upgrade("fasterFireRate3", True)
            
            # opens pause screen
            elif game_state == "game" and 710 <= x <= 710 + 80 \
            and 705 <= y <= 705 + 80:
                events["gameState"] = "paused"
            # resume button
            elif game_state == "paused" and 225 <= x <= 225 + 350 \
            and 275 <= y <= 275 + 100:
                events["gameState"] = "game"
            # restart button
            elif game_state == "paused" and 225 <= x <= 225 + 350 \
            and 400 <= y <= 400 + 100:
                events["restart"] = True
                events["gameState"] = "game"
            # return to main menu button
            elif game_state == "paused" and 225 <= x <= 225 + 350 \
            and 525 <= y <= 525 + 100:
                events["gameState"] = "menu"

            # changing settings
            # changing difficulty
            elif game_state == "settings" and 75 <= x <= 75 + 200 \
            and 312.5 <= y <= 312.5 + 100:
                change_difficulty("easy")
            elif game_state == "settings" and 300 <= x <= 300 + 200 \
            and 312.5 <= y <= 312.5 + 100:
                change_difficulty("normal")
            elif game_state == "settings" and 525 <= x <= 525 + 200 \
            and 312.5 <= y <= 312.5 + 100:
                change_difficulty("hard")
            # incrementing sensitivity
            elif game_state == "settings" and 475 <= x <= 525 \
            and 600 <= y <= 650:
                change_sensitivity(1)
            # decrementing sensitivity
            elif game_state == "settings" and 275 <= x <= 325 \
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