import pygame

def draw_text(screen, string: str, font: str, size: int, colour: tuple[int, int, int], bold: bool, coords: tuple[int, int]) -> None:
    text = pygame.font.SysFont(font, size, bold)
    rendered_text = text.render(string, True, colour)
    screen.blit(rendered_text, coords)