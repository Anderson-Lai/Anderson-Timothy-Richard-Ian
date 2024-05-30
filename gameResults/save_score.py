import json
from gameResults.getting.get_high_score import get_high_score
from gameResults.getting.get_score_file import get_score_file

def save_score(score: int) -> None:

    high_score = get_high_score()
    if score >= high_score:
        high_score = score

    score_file = get_score_file()

    score_file["highScore"] = high_score
    score_file["currentScore"] = score

    with open("score.json", "w") as file:
        json.dump(score_file, file)