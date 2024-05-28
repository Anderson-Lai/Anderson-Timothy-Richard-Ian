import json
from gameResults.create_score import create_score

def save_score(score: int) -> None:

    json_score = {
        "highScore": score,
    }

    with open("score.json", "w") as file:
        json.dump(json_score, file)