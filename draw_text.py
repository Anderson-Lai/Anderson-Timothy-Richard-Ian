import pygame

def draw_text(screen, string:str, font:str, size:int, colour:tuple, bold:bool, coords:tuple) -> None:
    text = pygame.font.SysFont(font, size, bold)
    rendered_text = text.render(string, True, colour)
    screen.blit(rendered_text, coords)