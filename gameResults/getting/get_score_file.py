import json

def get_score_file() -> dict:
    with open("./jsonFiles/score.json", "r") as file:
        score_file = json.load(file)
        return score_file