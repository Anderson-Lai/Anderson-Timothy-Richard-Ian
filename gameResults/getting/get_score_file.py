import json

def get_score_file() -> dict:
    with open("score.json", "r") as file:
        score_file = json.load(file)
        return score_file