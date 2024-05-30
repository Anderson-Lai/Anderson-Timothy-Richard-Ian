import json

def change_difficulty() -> None:
    difficulties = ["easy", "normal", "hard", "impossible"]

    file = open("settings.json", "r")
    settings = json.load(file)
    file.close()

    difficultyIndex = settings["difficultyIndex"]

    difficultyIndex += 1

    if difficultyIndex >= 4:
        difficultyIndex = 0
    
    settings["difficultyIndex"] = difficultyIndex
    settings["difficulty"] = difficulties[difficultyIndex]

    with open("settings.json", "w") as file:
        json.dump(settings, file)