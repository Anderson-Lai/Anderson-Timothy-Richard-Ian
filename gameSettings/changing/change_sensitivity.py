import json

def change_sensitivity(amount: int) -> None:
    file = open("./jsonFiles/settings.json", "r")
    settings = json.load(file)
    file.close()

    settings["sensitivity"] += amount

    if settings["sensitivity"] <= 0:
        settings["sensitivity"] = 1

    with open("./jsonFiles/settings.json", "w") as file:
        json.dump(settings, file)