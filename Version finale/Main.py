import os, sys, pygame, math, random
from pygame.locals import *

pygame.init()
screenData = pygame.display.Info()
MyScreen = pygame.display.set_mode(( math.floor(screenData.current_h/1.2), math.floor(screenData.current_h/1.2)), pygame.RESIZABLE)
size = [math.floor(screenData.current_h/1.2), math.floor(screenData.current_h/1.2)]

maps = pygame.image.load("plan_idee.png")
maprect = maps.get_rect()

DT = 0
Clocker = 0

GBL_arriverinter = False
GBL_Intervention = 1.1
GBL_StartVhc = 999
GBL_text_top = "        Status : en Attente"

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

vsav1 = vehicles(5, ['ambulance'], 'VSAV1', 'POMPIER', ['SAP'], 3, 2)
fptsr = vehicles(8, ['camion accidents','FPTSR', 'camion incendie'], 'FPTSR', 'POMPIER', ['AVP','INC','DIV'], 3, 2)

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


def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

###################################### Generation des intervention (from rémi, adapted by loulou) :

def generate_inters() :

    global GBL_Intervention
    global GBL_arriverinter
    global GBL_text_top

    GBL_arriverinter = False

    try_coords = [0,0]
    while try_coords == [0,0] :
        try_coords = [ random.randint(0, 41), random.randint(0, 41) ]
        if IsRoad(try_coords[0], try_coords[1]) != True or (try_coords == [1,2] or try_coords == [2,2] or try_coords == [3,2] or try_coords == [4,2]):
            try_coords = [0,0]

    inters = ["Accident VL", "Accident PL", "Blessure", "Malaise"]

    numero_inter = random.randint(0, (len (inters)-1))
    ### numero_renfort = random.randint(0, (len(renforts)-1))

    if numero_inter == 0: #accident routier VL
        GBL_Intervention = intervention(0, "AVP", try_coords[0], try_coords[1], 100, random.randint(15, 30))
        GBL_text_top = "        AVP : 1 VL seul"

    if numero_inter == 1: # AVP poid lourd
        GBL_Intervention = intervention(0, "AVP", try_coords[0], try_coords[1], 100, random.randint(20, 40))
        GBL_text_top = "        AVP : 1 PL + 1 VL"

    if numero_inter == 2: # Blessure lègere
        GBL_Intervention = intervention(0, "SAP", try_coords[0], try_coords[1], 100, random.randint(5, 15))
        GBL_text_top = "        SAP : Blessure de sport"

    if numero_inter == 3: # Malaise
        GBL_Intervention = intervention(0, "SAP", try_coords[0], try_coords[1], 100, random.randint(12, 22))
        GBL_text_top = "        SAP : Malaise au travail"

    
    return True


########################################################################

VSAV1 = pygame.image.load("vehicules\\VSAV2.png")
VSAV1rect = VSAV1.get_rect()
VSAV1_rot = False

FPTSR = pygame.image.load("vehicules\\FPTSR1.png")
FPTSRrect = FPTSR.get_rect()
FPTSR_rot = False


FS = pygame.image.load("icones\\firestation.png")
FSrect = FS.get_rect()

AVP_1 = pygame.image.load("icones\\icone AVP.png")
AVP_1rect = AVP_1.get_rect()

SAP_1 = pygame.image.load("icones\\icone SAP.png")
SAP_1rect = SAP_1.get_rect()


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
    Clocker = Clocker + DT

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

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if fpsps >= 0.3:
        compteur = compteur + 1

        if vsav1.hidden == False:
            if type(GBL_Intervention) != float :
                coord = Find_Next_Path(vsav1.x, vsav1.y, GBL_Intervention.x, GBL_Intervention.y)
                if [GBL_Intervention.x, GBL_Intervention.y] == [vsav1.x, vsav1.y] and GBL_arriverinter == False:
                    GBL_arriverinter = True
            else :
                coord = Find_Next_Path(vsav1.x, vsav1.y, 3, 2)
                if [3, 2] == [vsav1.x, vsav1.y]:
                    vsav1.hidden = True
            if coord == [vsav1.x - 1, vsav1.y]:
                VSAV1 = pygame.transform.rotate(pygame.image.load("vehicules\\VSAV2.png"), 180)
                VSAV1rect = VSAV1.get_rect()
                VSAV1_rot = False
            elif coord == [vsav1.x, vsav1.y + 1]:
                VSAV1 = pygame.transform.rotate(pygame.image.load("vehicules\\VSAV2.png"), 270)
                VSAV1rect = VSAV1.get_rect()
                VSAV1_rot = True
            elif coord == [vsav1.x, vsav1.y - 1]:
                VSAV1 = pygame.transform.rotate(pygame.image.load("vehicules\\VSAV2.png"), 90)
                VSAV1rect = VSAV1.get_rect()
                VSAV1_rot = True
            else:
                VSAV1 = pygame.image.load("vehicules\\VSAV2.png")
                VSAV1rect = VSAV1.get_rect()
                VSAV1_rot = False
            vsav1.move(coord[0], coord[1])

        if fptsr.hidden == False:
            if type(GBL_Intervention) != float :
                coord = Find_Next_Path(fptsr.x, fptsr.y, GBL_Intervention.x, GBL_Intervention.y)
                if [GBL_Intervention.x, GBL_Intervention.y] == [fptsr.x, fptsr.y] and GBL_arriverinter == False:
                    GBL_arriverinter = True
            else :
                coord = Find_Next_Path(fptsr.x, fptsr.y, 3, 2)
                if [3, 2] == [fptsr.x, fptsr.y]:
                    fptsr.hidden = True
            if coord == [fptsr.x - 1, fptsr.y]:
                FPTSR = pygame.transform.rotate(pygame.image.load("vehicules\\FPTSR1.png"), 180)
                FPTSRrect = FPTSR.get_rect()
                FPTSR_rot = False
            elif coord == [fptsr.x, fptsr.y + 1]:
                FPTSR = pygame.transform.rotate(pygame.image.load("vehicules\\FPTSR1.png"), 270)
                FPTSRrect = FPTSR.get_rect()
                FPTSR_rot = True
            elif coord == [fptsr.x, fptsr.y - 1]:
                FPTSR = pygame.transform.rotate(pygame.image.load("vehicules\\FPTSR1.png"), 90)
                FPTSRrect = FPTSR.get_rect()
                FPTSR_rot = True
            else:
                FPTSR = pygame.image.load("vehicules\\FPTSR1.png")
                FPTSRrect = FPTSR.get_rect()
                FPTSR_rot = False
            fptsr.move(coord[0], coord[1])
        fpsps = fpsps - 0.3
        
        if type(GBL_Intervention) == float and Clocker >= GBL_Intervention :
            generate_inters()
            GBL_Intervention.hidden = False
            fptsr.hidden = True
            vsav1.hidden = True
    
    VSAV1rect = MoveIt(VSAV1, 6.6, 2.2, vsav1.x, vsav1.y)

    FPTSRrect = MoveIt(FPTSR, 7.1, 2.5, fptsr.x, fptsr.y)

    if type(GBL_Intervention) != float:
        AVP_1rect = MoveIt(AVP_1, 1.5, 1.5, GBL_Intervention.x, GBL_Intervention.y)
        SAP_1rect = MoveIt(SAP_1, 1.5, 1.5, GBL_Intervention.x, GBL_Intervention.y)
        if GBL_arriverinter == True:
            GBL_Intervention.timer = GBL_Intervention.timer - DT
        if GBL_Intervention.timer <= 0 :
            player_XP = player_XP + GBL_Intervention.XP
            print("\n\nXP : ", player_XP, "\n\n")
            GBL_Intervention = Clocker + random.randint(10,30)
            GBL_text_top = "        Status : en Attente"


    ###################################################################

    MyScreen.fill((0,0,0)) # black background
    MyScreen.blit(pygame.transform.scale(maps, size), pygame.transform.scale(maps, size).get_rect()) # map display, don't touch

    ####################################################################
        #AFFICHAGE DES VEHICULES#


    if vsav1.hidden == False:
            # MyScreen.blit(ShowIt( name , width, height), namerect )
            if VSAV1_rot == False:
                MyScreen.blit(ShowIt(VSAV1, 0.66*3, 0.22*3), VSAV1rect)
            else:
                MyScreen.blit(ShowIt(VSAV1, 0.22*3, 0.66*3), VSAV1rect)

    
    if fptsr.hidden == False:
            # MyScreen.blit(ShowIt( name , width, height), namerect )
            if FPTSR_rot == False:
                MyScreen.blit(ShowIt(FPTSR, 0.71*3, 0.25*3), FPTSRrect)
            else:
                MyScreen.blit(ShowIt(FPTSR, 0.25*3, 0.71*3), FPTSRrect)

    
    if type(GBL_Intervention) != float and GBL_Intervention.hidden == False:
            # MyScreen.blit(ShowIt( name , width, height), namerect )
            if GBL_Intervention.typ == "AVP":
                MyScreen.blit(ShowIt(AVP_1, 1, 1.5), AVP_1rect)

            if GBL_Intervention.typ == "SAP":
                MyScreen.blit(ShowIt(SAP_1, 1, 1.5), SAP_1rect)
    
    FSrect = MoveIt(FS, 1.2*3, 1*3, 2, 2)
    MyScreen.blit(ShowIt(FS, 1.2*3, 1*3), FSrect)

    if 90 > mouse[0] > 10 and size[1] - 10 > mouse[1] > size[1] - 50:
        pygame.draw.rect(MyScreen, (150,150,150),(10,size[1] - 50,80,40))
        if click[0] == 1:
            vsav1.hidden = False
    else:
        pygame.draw.rect(MyScreen, (255,255,255),(10,size[1] - 50,80,40))

    if 90 > mouse[0] > 10 and size[1] - 60 > mouse[1] > size[1] - 100:
        pygame.draw.rect(MyScreen, (150,150,150),(10,size[1] - 100,80,40))
        if click[0] == 1:
            fptsr.hidden = False
    else:
        pygame.draw.rect(MyScreen, (255,255,255),(10,size[1] - 100,80,40))

    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(GBL_text_top, largeText)
    MyScreen.blit(TextSurf, TextRect)

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("VSAV", smallText)
    textRect.center = ( (10+(80/2)), (size[1] - 50+(40/2)) )
    MyScreen.blit(textSurf, textRect)

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects("FPTSR", smallText)
    textRect.center = ( (10+(80/2)), (size[1] - 100+(40/2)) )
    MyScreen.blit(textSurf, textRect)
    
    

    #####################################################################

    # affiche le tout
    pygame.display.flip()













## Un bon conseil : Ne touchez pas et ne regardez pas plus de 30s le code ci-dessous, sauf si tu est Chuck Norris, ou Linus Torvald, dans ce cas ça ira :)

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