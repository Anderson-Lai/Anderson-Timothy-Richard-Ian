import json

def get_difficulty() -> str:
    with open("./jsonFiles/settings.json") as file:
        settings = json.load(file)

        return settings["difficulty"]