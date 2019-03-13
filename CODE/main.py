import os, sys, pygame, math
from pygame.locals import *

pygame.init()
screenData = pygame.display.Info()
MyScreen = pygame.display.set_mode(( math.floor(screenData.current_w/2), math.floor(screenData.current_h/2)), pygame.RESIZABLE)
size = [math.floor(screenData.current_w/2), math.floor(screenData.current_h/2)]

maps = pygame.image.load("map2.png")
maprect = maps.get_rect()

# xxx = pygame.image.load(" filename.png ")
# xxxrect = xxx.get_rect()
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


def MoveIt(item, Wm, Hm, Xm, Ym):
    # size of map : 100x 50y
    itemRect = pygame.transform.scale(item, [ max(1,int(Wm * size[0] / 100)) , max(1,int(Hm * size[1] / 50)) ]).get_rect()
    itemRect.x = size[0] * Xm / 100
    itemRect.y = size[1] * Ym / 50
    return itemRect
def ShowIt(item, Wm, Hm):
    # size of map : 100x 50y
    return pygame.transform.scale(item, [ max(1,int(Wm * size[0] / 100)) , max(1,int(Hm * size[1] / 50)) ])



clock = pygame.time.Clock()

while 1:
    DT = clock.tick() / 1000
    # DT : Delta Time : temps entre 2 fps

    # gestion des events de type : resize de la fenetre et croix de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = [event.w, event.h]
            MyScreen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        else : print(event)

    # ci-dessous : le code de Update() qui bouge tout le bordel de l'écran

    # xxxrect = MoveIt(xxx , width, height, x, y)
    ballrect = MoveIt(ball, 25, 25, 12.5, 12.5)

    MyScreen.fill((0,0,0)) # black background
    MyScreen.blit(pygame.transform.scale(maps, size), pygame.transform.scale(maps, size).get_rect()) # map display, don't touch

    # MyScreen.blit(ShowIt( xxx , width, height), xxxrect )
    MyScreen.blit(ShowIt(ball, 25, 25), ballrect)

    # affiche le tout
    pygame.display.flip()




















## Un bon conseil : Ne touchez pas et ne regarder pas plus de 30s le code ci-dessous, sauf si tu est chuck norris, ou Linus Torvald, dans ce cas ça ira :)

""" pxtom = [ mapsize[0] / size[0] , mapsize[1] / size[1] ]
    mtopx = [ size[0] / mapsize[0] , size[1] / mapsize[1] ]

    speedSS = [ DT * speed[0] , DT * speed[1] ]

    ballrect = pygame.transform.scale(ball, [ max(1,int(0.5 * mtopx[0])) , max(1,int(0.5 * mtopx[1])) ]).get_rect()

    ballpos = [int(ballpos[0] + (speedSS[0] * mtopx[0])), int(ballpos[1] + (speedSS[1] * mtopx[1]))]
    ballrect.x = ballpos[0]
    ballrect.y = ballpos[1]
    if ballrect.left < 0 or ballrect.right > size[0]:
        speed[0] = -(speed[0] * 1)
    if ballrect.top < 0 or ballrect.bottom > size[1]:
        speed[1] = -(speed[1] * 1)

    maprect = pygame.transform.scale(maps, size).get_rect()
    maprect.x = 0
    maprect.y = 0

    MyScreen.fill((0,0,0))
    MyScreen.blit(pygame.transform.scale(maps, size), maprect)
    MyScreen.blit(pygame.transform.scale(ball, [ max(1,int(0.5 * mtopx[0])) , max(1,int(0.5 * mtopx[1])) ]), ballrect) """