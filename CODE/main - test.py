import os, sys, pygame, math, random
from pygame.locals import *

pygame.init()
screenData = pygame.display.Info()
MyScreen = pygame.display.set_mode(( math.floor(screenData.current_h/1.5), math.floor(screenData.current_h/1.5)), pygame.RESIZABLE)
size = [math.floor(screenData.current_h/1.5), math.floor(screenData.current_h/1.5)]

maps = pygame.image.load("plan_idee.png")
maprect = maps.get_rect()

#######################################################################
    #Classes

class intervention :
    "Intervention en cours ou fini"
  
    def __init__ (self, ID, typ, x, y, XP, time):
    ## (int) ID   -   (string) typ   -   (float) x   -   (float) y   -   (float) XP   -   (float) time 
        self.x = x
        self.y = y
        self.typ = typ ## (string) type = { INC, SAP, DIV, ... }
        self.ID = ID ### (int) ID unique = { 001, 002, 003, ... }
        self.fini = False # (bool) intervention non terminee 
        self.hidden = True
        self.XPmaxi = XP # (float) experience maximale a obtenir lors de l'intervention
        self.XP = XP # (float) experience que le joueur recevra à la fin de l'intervfention : change au court de celle-ci 
        self.timer = time ## (float) nombre de secondes avant la fin de l'intervention

    def open_menu(self):
        self.hidden = False

    def accept(self): # accepter une intervention 
        self.hidden = False
        self.fini = False

    def refuse (self): # refuser une intervention
        self.XP = 0
        self.close()
      
    def transmit(self, service): # donner l'ordre d'intervention a un autre service ## service : string = { SAMU, POLICE, ... }

        if service == 'POLICE':
            if self.typ == 'AVP' or self.typ == 'DIV':
                self.XP = self.XPmaxi*0.15
            elif self.typ == 'CRM' or self.typ == 'ARR' or self.typ == 'REN':
                self.XP = self.XPmaxi*0.25
            else:
                self.XP = 0
        
        if service == 'SAMU':
            if self.typ == 'AVP' or self.typ == 'SAP' or self.typ == 'REN':
                self.XP = self.XPmaxi*0.25
            else:
                self.XP = 0
        
        if service == 'POMPIER':
            if self.typ == 'DIV':
                self.XP = self.XPmaxi*0.15
            elif self.typ == 'INC' or self.typ == 'AVP' or self.typ == 'SAP' or self.typ == 'REN':
                self.XP = self.XPmaxi*0.25
            else:
                self.XP = 0


      
    def defer(self):  # remettre a plus tard une intervention
        self.hidden = True
        self.fini = False

    def close(self): # fini l'intervention ou l'annule 
        self.hidden = True
        self.fini = True



class vehicles :
    "vehicules de la caserne"
  
    def __init__(self, ID, typ, name, vhc_cat, capacites, x, y):
    # (int) ID - (string) typ - (string) name 
        self.x = x
        self.y = y
        self.type = typ ## (string) = { camion incendie, ambulance... }
        self.ID = ID ## (int) ID unique = { 001, 002, 003, ... }
        self.hidden = True ### (bool) afficher le vehicule: True = cache, False = affiche
        self.name = name ### (string) Nom complet du vehicule
        self.vhc_cat = vhc_cat ## (string) vhc_cat = { VSAV, FPT, ... }
        self.capacites = capacites ## capacites [] (string) = { SAP, INC, DIV, ... }


    def teleport (self, x, y): ### deplace le vehicule instantanément aux coordonnées x et y
    ## (float) x, y
        self.x = x
        self.y = y
    
    def move (self, x, y): # déplace le vehicule en fonction des coordonnees x et y
    ## (float) x, y
        self.x = x
        self.y = y

vsav1 = vehicles(5, ['ambulance'], 'VSAV1', 'POMPIER', ['SAP'], 1, 2)
fptsr = vehicles(8, ['camion accidents','FPTSR', 'camion incendie'], 'FPTSR', 'POMPIER', ['AVP','INC','DIV'], 4, 2)
avp_1 = intervention(3, "AVP", 39, 39, 100, 100)

########################################################################
#fonction chemin

MAP_PATH = [
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 0,0,0,1,1, 0,0],
 [0,1,1,1,1, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,1,1,1,1, 1,0,0,0,0, 0,0,1,1,1, 0,0],
 [0,0,0,0,1, 1,1,1,1,0, 0,0,0,0,0, 0,0,1,1,1, 1,1,1,1,1, 0,0,0,0,1, 1,1,1,0,0, 0,1,1,1,0, 0,0],
 [0,0,0,0,0, 0,0,1,1,1, 1,1,1,1,1, 1,1,1,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,1,1,1, 1,1,0,0,0, 0,0],
 [0,0,0,0,0, 0,0,0,0,0, 0,1,1,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,0,0,0,0, 0,0],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,1,1,1,0, 0,0],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,1,1,0,0, 0,0,1,1,1, 1,0],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,0,0, 0,0,0,0,1, 1,1,1,1,1, 1,1,1,1,1, 1,0,0,0,0, 1,1],
 [0,0,0,0,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,0,0,0,0, 1,1,0,1,1, 1,1,1,1,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 1,1,0,0,0, 0,1,1,1,1, 1,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 1,0,0,0,0, 0,0,0,0,1, 1,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,1,1, 0,1,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 1,1,1,1,1, 1,1,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 1,1,0,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 1,1,1,1,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,1, 1,0,0,1,1, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,1,1, 0,0,0,0,1, 1,0,0,0,0, 0,0],
 [0,1,1,0,1, 0,0,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 1,0,0,0,0, 0,0],
 [0,1,1,1,1, 0,0,0,1,1, 1,0,0,0,0, 0,0,0,0,0, 1,0,0,0,0, 1,1,1,0,0, 0,0,0,0,0, 1,1,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,1, 1,1,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 1,1,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,1,1,1,1, 1,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,1,1, 0,0,0,0,0, 1,0,0,0,0, 0,0,0,1,1, 1,1,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,0,0,1, 0,0,0,0,0, 1,0,0,0,0, 1,1,1,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 0,0,0,0,0, 0,0,1,0,0, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,1, 1,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,0, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0],
 [0,0,0,0,0, 1,1,0,0,0, 0,0,0,0,0, 0,0,0,0,1, 1,0,0,0,0, 0,0,0,0,0, 0,0,1,1,1, 1,1,1,1,1, 0,0],
 [0,0,0,0,0, 0,1,1,0,0, 0,0,0,1,1, 1,1,1,1,1, 1,1,0,0,0, 0,0,0,0,0, 0,1,1,1,0, 0,0,0,0,1, 1,0],
 [0,0,0,0,0, 0,0,1,1,1, 1,1,1,1,1, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 1,1],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,1],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 0,1,1,0,0, 0,0,0,0,0, 0,1],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,1,1,1,1, 1,1,1,1,0, 0,0,0,0,0, 1,1],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 1,1,1,1,1, 1,0,0,0,1, 1,1],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,1, 1,1,1,0,1, 1,1],
 [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,1, 1,1]
]


def IsRoad(x,y):
    if MAP_PATH[y][x] == 1:
        return True
    else:
        return False


def Find_Path (x1, y1, x2, y2):
    if (IsRoad(x1,y1) == True and IsRoad(x2,y2) == True) and (x1 == x2 and y1 == y2) == False:
        # Level 1 : listes des chemins / Level 2 : listes des cases dans l'ordre du chemin / Level 3 : combo point x et y
        Paths = [
            [[x1,y1]]
        ]
        # Liste de points sur lequel on est passé
        PassedOn = [[x1,y1]]
        Finded = False
        i = 0
        while Finded == False:
            i = 0
            for oneeePath in Paths:
                onePath = oneeePath.copy()
                originalPathModified = False

                # x + 1  : vers la droite
                # si la case existe ET que c'est une route
                if (onePath[-1][0] + 1) <= 41 and MAP_PATH[ onePath[-1][1] ][ onePath[-1][0] + 1 ] == 1:
                    # est on deja passer par la ?
                    if [ onePath[-1][0] + 1 , onePath[-1][1] ] in PassedOn:
                        # on est deja passer par cette case, skip
                        i = i
                    else:
                        # on ajoute la case dans le tableau des case deja utiliser
                        PassedOn.append([ onePath[-1][0] + 1 , onePath[-1][1] ])
                        # on ajoute la case dans le chemin en cours
                        Paths[i].append([onePath[-1][0] + 1 , onePath[-1][1]])
                        originalPathModified = True
                        if (onePath[-1][0] + 1) == x2 and onePath[-1][1] == y2:
                            Finded = True
                            return Paths[i]


                # x - 1  :  vers la gauche
                if (onePath[-1][0] - 1) >= 0 and MAP_PATH[ onePath[-1][1] ][ onePath[-1][0] - 1 ] == 1:
                    if [ onePath[-1][0] - 1 , onePath[-1][1] ] in PassedOn:
                        i = i
                    else:
                        PassedOn.append([ onePath[-1][0] - 1 , onePath[-1][1] ])
                        if originalPathModified == True:
                            Paths.append(  onePath.copy()  )
                            Paths[-1].append([onePath[-1][0] - 1 , onePath[-1][1]])
                            if (onePath[-1][0] - 1) == x2 and onePath[-1][1] == y2:
                                Finded = True
                                return Paths[-1]
                        else:
                            Paths[i].append([onePath[-1][0] - 1 , onePath[-1][1]])
                            originalPathModified = True
                            if (onePath[-1][0] - 1) == x2 and onePath[-1][1] == y2:
                                Finded = True
                                return Paths[i]


                # y + 1  :  vers le bas
                if (onePath[-1][1] + 1) <= 41 and MAP_PATH[ onePath[-1][1] + 1 ][ onePath[-1][0] ] == 1:
                    if [ onePath[-1][0] , onePath[-1][1] + 1 ] in PassedOn:
                        i = i
                    else:
                        PassedOn.append([ onePath[-1][0] , onePath[-1][1] + 1 ])
                        if originalPathModified == True:
                            Paths.append(  onePath.copy()  )
                            Paths[-1].append([onePath[-1][0] , onePath[-1][1] + 1])
                            if onePath[-1][0] == x2 and (onePath[-1][1] + 1) == y2:
                                Finded = True
                                return Paths[-1]
                        else:
                            Paths[i].append([onePath[-1][0] , onePath[-1][1] + 1])
                            originalPathModified = True
                            if onePath[-1][0] == x2 and (onePath[-1][1] + 1) == y2:
                                Finded = True
                                return Paths[i]


                # y - 1  :  vers le haut
                if (onePath[-1][1] - 1) >= 0 and MAP_PATH[ onePath[-1][1] - 1 ][ onePath[-1][0] ] == 1:
                    if [ onePath[-1][0] , onePath[-1][1] - 1 ] in PassedOn:
                        i = i
                    else:
                        PassedOn.append([ onePath[-1][0] , onePath[-1][1] - 1 ])
                        if originalPathModified == True:
                            Paths.append(  onePath.copy()  )
                            Paths[-1].append([onePath[-1][0] , onePath[-1][1] - 1])
                            if onePath[-1][0] == x2 and (onePath[-1][1] - 1) == y2:
                                Finded = True
                                return Paths[-1]
                        else:
                            Paths[i].append([onePath[-1][0] , onePath[-1][1] - 1])
                            originalPathModified = True
                            if onePath[-1][0] == x2 and (onePath[-1][1] - 1) == y2:
                                Finded = True
                                return Paths[i]
                i = i + 1
    else: 
        return "Error"


def Find_Next_Path(x, y, xd, yd):
    res = Find_Path(x,y,xd,yd)
    if res == "Error":
        return [x,y]
    else:
        return res[1]

"""
print(Find_Next_Path(2,1 , 14,12)[0])
total = 0
for j in range(0,0):
    a = random.randint(0,41)
    b = random.randint(0,41)
    c = random.randint(0,41)
    d = random.randint(0,41)
    if(IsRoad(a,b) and IsRoad(c,d)):
        total = total + 1
        print(a,b,c,d, sep=' | ')
        if Find_Path(a,b,c,d) == "error":
            print("error occured")
            break
    print(total)
print("finished with : " + str(total))
"""

########################################################################

VSAV1 = pygame.image.load("vehicules\\VSAV2.png")
VSAV1rect = VSAV1.get_rect() 

FPTSR = pygame.image.load("vehicules\\FPTSR1.png")
FPTSRrect = FPTSR.get_rect()

AVP_1 = pygame.image.load("icones\\icone AVP.png")
AVP_1rect = AVP_1.get_rect()



########################################################################

def MoveIt(item, Wm, Hm, Xm, Ym):
    # size of map : 20x 20y
    itemRect = pygame.transform.scale(item, [ max(1,int(Wm * size[0] / 42)) , max(1,int(Hm * size[1] / 42)) ]).get_rect()
    itemRect.x = size[0] * Xm / 42
    itemRect.y = size[1] * Ym / 42
    return itemRect
def ShowIt(item, Wm, Hm):
    # size of map : 20x 20y
    return pygame.transform.scale(item, [ max(1,int(Wm * size[0] / 42)) , max(1,int(Hm * size[1] / 42)) ])

player_XP = 0

clock = pygame.time.Clock()

fpsps = 0
compteur = 0



while 1:
    DT = clock.tick() / 1000
    # DT : Delta Time : temps entre 2 fps
    fpsps = fpsps + DT
    # gestion des events de type : resize de la fenetre et croix de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = [event.w, event.h]
            MyScreen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        #else : print(event)

    # ci-dessous : le code de Update() qui bouge tout le bordel de l'écran

    ###################################################################
        #TAILLE ET POSITON (DANS LE TPS) DES VEHICULES#

    #'NAME'rect = MoveIt('NAME', width, height, x, y) #coordonées fournies par la fonction 'PATH'
    #largeurs: camion = 2.5, camionnette = 2, ambulance 'cube' = 2.2, VL = 1.8 ou 2

    if fpsps >= 0.3:
        compteur = compteur + 1
        if vsav1.hidden == False:
            coord = Find_Next_Path(vsav1.x, vsav1.y, 39, 40)
            vsav1.move(coord[0], coord[1])
        if fptsr.hidden == False:
            coord = Find_Next_Path(fptsr.x, fptsr.y, 39, 39)
            fptsr.move(coord[0], coord[1])
        fpsps = fpsps - 0.3
        if compteur > 3:
            avp_1.hidden = False
        if compteur > 7:
            fptsr.hidden = False
        if compteur > 15:
            vsav1.hidden = False
    
    VSAV1rect = MoveIt(VSAV1, 6.6, 2.2, vsav1.x, vsav1.y)

    FPTSRrect = MoveIt(FPTSR, 7.1, 2.5, fptsr.x, fptsr.y)

    AVP_1rect = MoveIt(AVP_1, 1, 1.5, 39, 39)


    ###################################################################

    MyScreen.fill((0,0,0)) # black background
    MyScreen.blit(pygame.transform.scale(maps, size), pygame.transform.scale(maps, size).get_rect()) # map display, don't touch

    ####################################################################
        #AFFICHAGE DES VEHICULES#


    if vsav1.hidden == False:
            # MyScreen.blit(ShowIt( name , width, height), namerect )
            MyScreen.blit(ShowIt(VSAV1, 0.66*3, 0.22*3), VSAV1rect)

    
    if fptsr.hidden == False:
            # MyScreen.blit(ShowIt( name , width, height), namerect )
            MyScreen.blit(ShowIt(FPTSR, 0.71*3, 0.25*3), FPTSRrect)

    
    if avp_1.hidden == False:
            # MyScreen.blit(ShowIt( name , width, height), namerect )
            MyScreen.blit(ShowIt(AVP_1, 1, 1.5), AVP_1rect)

    

    #####################################################################

    # affiche le tout
    pygame.display.flip()




















## Un bon conseil : Ne touchez pas et ne regarder pas plus de 30s le code ci-dessous, sauf si tu est Chuck Norris, ou Linus Torvald, dans ce cas ça ira :)

""" pxtom = [ mapsize[0] / size[0] , mapsize[1] / size[1] ]
    mtopx = [ size[0] / mapsize[0] , size[1] / mapsize[1] ]
    speedSS = [ DT * speed[0] , DT * speed[1] ]
    VSAVrect = pygame.transform.scale(VSAV, [ max(1,int(0.5 * mtopx[0])) , max(1,int(0.5 * mtopx[1])) ]).get_rect()
    VSAVpos = [int(VSAVpos[0] + (speedSS[0] * mtopx[0])), int(VSAVpos[1] + (speedSS[1] * mtopx[1]))]
    VSAVrect.x = VSAVpos[0]
    VSAVrect.y = VSAVpos[1]
    if VSAVrect.left < 0 or VSAVrect.right > size[0]:
        speed[0] = -(speed[0] * 1)
    if VSAVrect.top < 0 or VSAVrect.bottom > size[1]:
        speed[1] = -(speed[1] * 1)
    maprect = pygame.transform.scale(maps, size).get_rect()
    maprect.x = 0
    maprect.y = 0
    MyScreen.fill((0,0,0))
    MyScreen.blit(pygame.transform.scale(maps, size), maprect)
    MyScreen.blit(pygame.transform.scale(VSAV, [ max(1,int(0.5 * mtopx[0])) , max(1,int(0.5 * mtopx[1])) ]), VSAVrect) """