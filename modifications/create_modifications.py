import json


def create_modifications() -> None:
    
    settings = {
        # power ups
        "doubleShot": False,
        "multiShot": False,
        "extraLife": False,
        "fasterFireRate1": False,
        "fasterFireRate2": False,
        "fasterFireRate3": False,
        # cosmetics
        "shipColour": "green", "red"
        # coins
        "coins": 0
    }

    try:
        with open("./jsonFiles/modifications.json", "r") as file:
            pass
    except FileNotFoundError:
        with open("./jsonFiles/modifications.json", "w") as file:
            json.dump(settings, file)
