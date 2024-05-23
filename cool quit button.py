font = pygame.font.SysFont('Arial',40,bold=True)
surf = font.render('Quit', True, 'white')
button = pygame.Rect(200,200,110,60)

   
x,y = pygame.mouse.get_pos()
if button.x <= x <= button.x + 110 and button.y <= y <= button.y +60:
    pygame.draw.rect(screen,(180,180,180),button )
else:
    pygame.draw.rect(screen, (110,110,110),button)
screen.blit(surf,(button.x +5, button.y+5))
