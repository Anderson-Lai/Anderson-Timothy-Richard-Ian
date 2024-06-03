import json

def change_difficulty(difficulty:str) -> None:
                # OLD CODE #
    # difficulties = ["easy", "normal", "hard"]

    file = open("./jsonFiles/settings.json", "r")
    settings = json.load(file)
    file.close()

    settings["difficulty"] = difficulty

                # OLD CLODE #
    # difficultyIndex = settings["difficultyIndex"]

    # difficultyIndex += 1

    # if difficultyIndex >= 3:
    #     difficultyIndex = 0
    
    # settings["difficultyIndex"] = difficultyIndex
    # settings["difficulty"] = difficulties[difficultyIndex]

    with open("./jsonFiles/settings.json", "w") as file:
        json.dump(settings, file)