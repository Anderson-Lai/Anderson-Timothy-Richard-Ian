import pygame
from gameSettings.changing.change_difficulty import change_difficulty
from gameSettings.changing.change_sensitivity import change_sensitivity
from gameSettings.getting.get_sensitivity import get_sensitivity
from gameSettings.getting.get_difficulty import get_difficulty
from modifications.getting.get_coins import get_coins
from modifications.changing.change_upgrade import change_upgrade
from modifications.changing.change_coins import change_coins
from modifications.getting.get_upgrade_state import get_upgrade_state

def handle_events(events: dict):

    game_state: str = events["gameState"]
    location: int = events["location"]
    # destructuring events["running"] should not be necessary
    # as it should only be used once in the pygame.QUIT event

    coins = get_coins()
    sensitivity = get_sensitivity()
    difficulty = get_difficulty()

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
            elif game_state == "shop" and 612.5 <= x <= 612.5 + 100 \
            and 210 <= y <= 210 + 65:
                if get_upgrade_state("doubleShot"):
                    pass
                elif coins >= 1000:
                    change_upgrade("doubleShot", True)
                    change_coins(-1000)
                    
            # multi shot
            elif game_state == "shop" and 612.5 <= x <= 612.5 + 100 \
            and 300 <= y <= 300 + 65:
                if get_upgrade_state("multiShot"):
                    pass
                elif coins >= 1500:
                    change_upgrade("multiShot", True)
                    change_coins(-1500)
            # extra life
            elif game_state == "shop" and 612.5 <= x <= 612.5 + 100 \
            and 390 <= y <= 390 + 65:
                if get_upgrade_state("extraLife"):
                    pass
                elif coins >= 2500:
                    change_upgrade("extraLife", True)
                    change_coins(-2500)
            # faster fire rate 1
            elif game_state == "shop" and 612.5 <= x <= 612.5 + 100 \
            and 480 <= y <= 480 + 65:
                if get_upgrade_state("fasterFireRate1"):
                    pass
                elif coins >= 1500:
                    change_upgrade("fasterFireRate1", True)
                    change_coins(-1500)
            # faster fire rate 2
            elif game_state == "shop" and 612.5 <= x <= 612.5 + 100 \
            and 570 <= y <= 570 + 65:
                if get_upgrade_state("fasterFireRate2"):
                    pass
                elif coins >= 3000:
                    change_upgrade("fasterFireRate2", True)
                    change_coins(-3000)
            # faster fire rate 3
            elif game_state == "shop" and 612.5 <= x <= 612.5 + 100 \
            and 660 <= y <= 660 + 65:
                if get_upgrade_state("fasterFireRate3"):
                    pass
                elif coins >= 5000:
                    change_upgrade("fasterFireRate3", True)
                    change_coins(-5000)       
            # returns to menu
            elif game_state == "shop" and 50 <= x <= 50 + 125 \
            and 50 <= y <= 50 + 125:
                events["gameState"] = "menu"
            
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
            # return to main menu when you die
            elif game_state == "dead" and 225 <= x <= 225 + 350 \
            and 525 <= y <= 525 + 100:
                events["gameState"] = "menu"
            # restart when you die
            elif game_state == "dead" and 225 <= x <= 225 + 350 \
            and 400 <= y <= 400 + 100:
                events["restart"] = True
                events["gameState"] = "game"
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
            if event.key == pygame.K_RIGHT and location <= 550:
                events["location"] += sensitivity

                if location + sensitivity >= 550:
                    events["location"] = 550
            # move left
            elif event.key == pygame.K_LEFT and location >= 20:
                events["location"] -= sensitivity
                
                if location - sensitivity <= 20:
                    events["location"] = 20
