from json import dump

def create_settings():
    default_settings = {
        "difficulty": "normal",
        "sensitivity": 10,
    }

    try:
        with open("./jsonFiles/settings.json", "r") as file:
            pass
    except FileNotFoundError:
        with open("./jsonFiles/settings.json", "w") as file:
            dump(default_settings, file)