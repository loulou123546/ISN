import random

MAP_PATH = [
    #0   2   4  5       9      12    15    18 19
    [0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,1,0],
    [1,1,1,1,1, 0,0,1,1,1, 1,1,1,1,1, 1,0,1,1,0],
    [0,0,0,0,1, 1,1,1,0,0, 0,0,0,0,0, 1,1,1,0,0],
    [0,0,0,0,0, 1,0,0,0,0, 0,0,0,1,1, 1,0,1,1,1],
    [0,0,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,0],

    [0,0,1,0,0, 0,0,0,0,1, 0,0,0,1,0, 0,0,0,1,1],
    [0,0,1,0,0, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,0],
    [0,0,1,0,0, 0,0,0,0,1, 1,1,1,1,1, 1,0,0,0,0],
    [0,0,1,0,0, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,0],
    [0,0,1,0,0, 0,0,0,0,1, 0,0,0,1,1, 0,1,0,0,0],

    [1,1,1,1,1, 0,0,0,0,1, 0,1,1,1,0, 0,1,0,0,0],
    [0,0,1,0,1, 1,0,0,0,1, 1,1,0,0,0, 1,1,1,0,0],
    [0,0,1,0,0, 1,0,0,0,1, 0,1,1,1,1, 1,0,0,0,0],
    [0,0,1,0,0, 1,1,1,1,1, 1,1,0,0,0, 0,0,0,0,0],
    [0,0,1,0,0, 0,0,0,1,0, 0,0,0,0,0, 0,0,0,0,0],

    [0,0,1,1,0, 0,0,0,1,1, 0,0,0,0,0, 1,1,1,1,0],
    [0,0,0,1,1, 1,1,1,1,1, 1,0,0,0,1, 1,0,0,1,1],
    [0,0,0,0,0, 0,0,0,0,0, 1,1,0,0,0, 1,0,0,0,1],
    [0,0,0,0,0, 0,0,0,0,0, 0,1,1,1,1, 1,1,0,1,1],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,1,1,0]
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
                if (onePath[-1][0] + 1) <= 19 and MAP_PATH[ onePath[-1][1] ][ onePath[-1][0] + 1 ] == 1:
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
                if (onePath[-1][1] + 1) <= 19 and MAP_PATH[ onePath[-1][1] + 1 ][ onePath[-1][0] ] == 1:
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
    if res == "error":
        return []
    else:
        return res[1]

"""
print(Find_Next_Path(2,1 , 14,12)[0])


total = 0
for j in range(0,0):
    a = random.randint(0,19)
    b = random.randint(0,19)
    c = random.randint(0,19)
    d = random.randint(0,19)
    if(IsRoad(a,b) and IsRoad(c,d)):
        total = total + 1
        print(a,b,c,d, sep=' | ')
        if Find_Path(a,b,c,d) == "error":
            print("error occured")
            break
    print(total)
print("finished with : " + str(total))
"""
