import json

def create_cosmetics() -> None:
    
    json_cosmetics = {

    }

    try:
        with open("cosmetics.json", "r") as file:
            pass    
    except FileNotFoundError:
        with open("cosmetics.json", "w") as file:
            json.dump(json_cosmetics, file)