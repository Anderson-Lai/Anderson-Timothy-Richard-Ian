import json

def create_score() -> None:

    score_json = {
        "highScore": 0,
    }

    try:
        with open("score.json", "r") as file:
            pass
    except FileNotFoundError:
        with open("score.json", "w") as file:
            json.dump(score_json, file)