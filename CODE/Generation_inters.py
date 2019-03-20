# 20 interventions
inters = ["accident routier sur autoroute", "cambriolage", "voiture mal stationee", "tentative de meurtre", "convoi", "personnne disparue", "feu de foret", "feu en ville", "arret cardique", "blessure en montage", "animal coince", "feu en zone maritime (port)", "zone de controle radar", "accident routier non autoroute", "blessure/malaise", "fuite de gaz", "incident ligne EDF", "arrestation d'un suspect", "incident chimique/nucleaire"]
import random
numero_inter = random.randint(0, len (inters))

def generate_inters() : 
    return inters[numero_inter] 

print(generate_inters())

    


