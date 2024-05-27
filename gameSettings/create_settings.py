from json import dump

def create_settings():
    default_settings = {
        "difficulty": "easy",
        "difficultyIndex": 0,
        "sensitivity": 10,
    }

    try:
        file = open("settings.json", "r")
    except FileNotFoundError:
        file = open("settings.json", "w")
        dump(default_settings, file)
    file.close()