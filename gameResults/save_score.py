import json
from create_score import create_score

def save_score(score: int) -> None:
    create_score()

    with open("score.json", "r") as file:
        score_json = json.load(file)
    
        score_json["highScore"] = score
        json.dump(score_json, file)