import json


def get_coins() -> int:
    with open("./jsonFiles/modifcations.json", "r") as file:
        settings = json.load(file)
        return settings["coins"]