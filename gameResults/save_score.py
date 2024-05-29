import json
from gameResults.get_high_score import get_high_score

def save_score(score: int) -> None:

    high_score = get_high_score()
    if score >= high_score:
        high_score = score

    json_score = {
        "highScore": high_score,
        "currentScore": score,
    }

    with open("score.json", "w") as file:
        json.dump(json_score, file)