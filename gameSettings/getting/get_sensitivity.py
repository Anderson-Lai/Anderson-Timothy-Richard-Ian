import json

def get_sensitivity() -> int:

    with open("./json/settings.json", "r") as file:
        settings = json.load(file)
        return settings["sensitivity"]