from textDrawing.draw_text import draw_text

def draw_money(screen, money:int, coordinates:tuple, size:int) -> None:
    # draws money
    draw_text(screen, f"${money}", "sfnsmono", size ,(255, 255, 0), False, coordinates)