import json

def create_cosmetics() -> None:
    
    json_cosmetics = {
        # colours
        "red": False,
        "orange": False,
        "yellow": False,
        "green": False,
        "blue": False,
        "purple": False,
        "white": False,
        "black": False,
        "rainbow": False,
        "pink": False,
        "brown": False,
        "aqua": False,
        "gray": False,

        # skins
        "leo": False,
        "eric": False,
    }

    try:
        with open("./jsonFiles/cosmetics.json", "r") as file:
            pass    
    except FileNotFoundError:
        with open("./jsonFiles/cosmetics.json", "w") as file:
            json.dump(json_cosmetics, file)