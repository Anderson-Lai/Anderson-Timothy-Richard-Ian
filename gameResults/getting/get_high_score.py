import json

def get_high_score() -> int:
    with open("score.json", "r") as file:
        score = json.load(file)
        return score["highScore"]