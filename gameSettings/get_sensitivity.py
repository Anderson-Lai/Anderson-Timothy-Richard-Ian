import json

def get_sensitivity() -> int:

    with open("settings.json", "r") as file:
        settings = json.load(file)
        return settings["sensitivity"]