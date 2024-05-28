import json

def get_settings() -> dict:

    with open("settings.json", "r") as file:
        settings = json.load(file)
        return settings