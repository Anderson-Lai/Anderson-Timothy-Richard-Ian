import json

def create_cosmetics() -> None:
    
    json_cosmetics = {
        # colours
        "shipColour": "green",
    }

    try:
        with open("./jsonFiles/cosmetics.json", "r") as file:
            pass    
    except FileNotFoundError:
        with open("./jsonFiles/cosmetics.json", "w") as file:
            json.dump(json_cosmetics, file)