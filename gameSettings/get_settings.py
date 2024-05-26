import json

def get_settings() -> dict:
    
    file = open("gameSettings/settings.json")

    settings = json.load(file)
    return settings