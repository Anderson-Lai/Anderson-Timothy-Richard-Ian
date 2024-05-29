import json

def create_powerups() -> None:
    
    json_powerups = {

    }

    try:
        with open("powerups.json", "r") as file:
            pass    
    except FileNotFoundError:
        with open("powerups.json", "w") as file:
            json.dump(json_powerups, file)