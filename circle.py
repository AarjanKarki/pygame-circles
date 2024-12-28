import pygame
pygame.init()
from math import pi

screen=pygame.display.set_mode((600,600))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill('red') 
    pygame.draw.circle(screen,(255,255,255),[300,300],160,10)
    pygame.draw.rect(screen,(255,255,255),[150,150,75,50],5)
    pygame.draw.ellipse(screen,(255,255,0),[400,400,150,75],0)
    #pygame.draw.arc(screen,(0,255,255),[25,25,90,180],0.0,90.0,5)
    x, y  = 150,150
    angle = (x/639.)*pi*2.0
    pygame.draw.arc(screen, (0,0,0), (0,0,639,479), 0, angle)
    pygame.display.flip()




pygame.quit()