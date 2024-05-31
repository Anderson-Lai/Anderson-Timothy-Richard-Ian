import json

def create_powerups() -> None:
    
    json_powerups = {
        "doubleShot": False,
        "multiShot": False,
        "extraLife": False,
        "fasterFireRate1": False,
        "fasterFireRate2": False,
        "fasterFireRate3": False,
    }

    try:
        with open("powerups.json", "r") as file:
            pass    
    except FileNotFoundError:
        with open("powerups.json", "w") as file:
            json.dump(json_powerups, file)