import pygame
import json

def game_settings(screen):
    screen.fill((255, 0, 0))

    sensitivity: int = 1
    difficulty: str = "test"

    settings = {
        "sensitivity": sensitivity,
        "difficulty": difficulty,
    }
    
    # opens file and truncates it
    file = open("settings.txt", "w")
    # write the settings to the file
    json.dump(settings, file)

    # cleanup
    file.close()

    # go back to main menu
    pygame.draw.rect(screen, (144, 238, 144), pygame.Rect(50, 50, 125, 125))