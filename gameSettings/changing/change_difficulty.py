import json

def change_difficulty(difficulty: str) -> None:
                # OLD CODE #
    # difficulties = ["easy", "normal", "hard"]
    # difficultyIndex = settings["difficultyIndex"]

    # difficultyIndex += 1

    # if difficultyIndex >= 3:
    #     difficultyIndex = 0
    
    # settings["difficultyIndex"] = difficultyIndex
    # settings["difficulty"] = difficulties[difficultyIndex]
    
    with open("./jsonFiles/settings.json", "r") as file:
        settings = json.load(file)
        settings["difficulty"] = difficulty;

    with open("./jsonFiles/settings.json", "w") as file:
        json.dump(settings, file)