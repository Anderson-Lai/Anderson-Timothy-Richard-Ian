import json

def get_difficulty() -> str:
    with open("./json/settings.json") as file:
        settings = json.load(file)

        return settings["difficulty"]