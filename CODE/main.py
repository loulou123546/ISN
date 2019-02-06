import os, sys, pygame, math
from pygame.locals import *

pygame.init()
screenData = pygame.display.Info()
MyScreen = pygame.display.set_mode(( math.floor(screenData.current_w/2), math.floor(screenData.current_h/2)), pygame.RESIZABLE)

size = [math.floor(screenData.current_w/2), math.floor(screenData.current_h/2)]

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

speed = [1,1]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = [event.w, event.h]
            MyScreen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        else : print(event)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > size[0]:
        speed[0] = -(speed[0] * 1)
    if ballrect.top < 0 or ballrect.bottom > size[1]:
        speed[1] = -(speed[1] * 1)

    MyScreen.fill((0,0,0))
    MyScreen.blit(ball, ballrect)

    pygame.display.flip()
