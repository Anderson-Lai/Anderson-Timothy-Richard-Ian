import json

def get_settings() -> dict:
    
    file = open("settings.json")

    settings = json.load(file)
    file.close()
    return settings