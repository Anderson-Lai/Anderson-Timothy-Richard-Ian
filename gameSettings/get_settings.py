import json

"""
there is no reason to ever use this over
try to avoid using this function
get_difficulty() or get_sensitivity()
these functions avoid the possibility of 
accidentally changing "difficultyIndex",
which may break the difficulty settings
"""
def get_settings() -> dict:

    with open("settings.json", "r") as file:
        settings = json.load(file)
        return settings