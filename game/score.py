from draw_text import draw_text

def get_score(enemy_kills: int) -> int:
    gain = 10
    score = gain * enemy_kills

    if score <= 0:
        return 0
    return score

def draw_score(screen, high_score:int, current_score:int) -> None:
    #draws high score
    draw_text(screen, f"HI: {high_score}", "sfnsmono", 30 ,(255, 255, 255), False, (625, 35))
    #draws current score
    draw_text(screen, f"{current_score}", "sfnsmono", 30 ,(255, 255, 255), False, (625, 95))