# Rémi
## Louis
### Romain

### Compte le temps depuis le lancement du jeu en secondes
Global Timer (float)

### Tableau contenant des instances de la classe "vehicule"
Global Vehicles [] (vehicles)

# Tableau contenant des insatnces de la classe "intervention" 
Global Intervention [] (intervention)

## Tableau contenant tous les messages textuels ou index le plus petit => message le plus vieux
Global Radio [] (string)

# Tableau contenant les noms des vehicules et les capacites de ceux-ci
Global Const Vehicles_Skills ['vehicle_name'] (vehicle_skills)

### Xp obtenu par le joueur depuis le lancement du jeu ou la création de la sauvegarde
Global Joueur_XP = 0 




## Classe 'vehicles'

class vehicles :
  "vehicules de la caserne"
  
  def __init__(self, ID, typ, name):
    # (int) ID - (string) typ - (string) name 
    self.x = 0
    self.y = 0
    self.type = typ ## (string) = { FPT, VSAV, VL, ... }
    self.ID = ID ## (int) ID unique = { 001, 002, 003, ... }
    self.hidden = True ### (bool) afficher le vehicule: True = affiché, False = caché
    self.name = name ### (string) Nom complet du vehicule
    
  def teleport (self, x, y): ### deplace le vehicule instantanément aux coordonnées x et y
    ## (float) x, y
    
  
  def move (self, x, y): # déplace le vehicule en fonction des coordonnees x et y
    ## (float) x, y
    


    
## Classe 'vehicles_skills'

class vehicles_skills :
  "capacites des vehicules"
  
  def __init__(self, vhc_cat, capacites) :
    ## (string) vhc_cat = { VSAV, FPT, ... }    -   capacites [] (string) = { SAP, INC, DIV, ... }
    self.x = 0
    self.y = 0
    self.vhc_cat = vhc_cat ## (string) vhc_cat = { VSAV, FPT, ... }
    self.capacites = capacites ## capacites [] (string) = { SAP, INC, DIV, ... }
    


    

## classe 'intervention'

class intervention :
  "Intervention en cours ou fini"
  
  def __init__ (self, ID, typ, x, y, XP, time):
    ## (int) ID   -   (string) typ   -   (float) x   -   (float) y   -   (float) XP   -   (float) time 
    self.x = 0
    self.y = 0
    self.typ = typ ## (string) type = { INC, SAP, DIV, ... }
    self.ID = ID ### (int) ID unique = { 001, 002, 003, ... }
    self.fini = False # (bool) intervention non terminee 
    self.XPmaxi = XP # (float) experience maximale a obtenir lors de l'intervention
    self.XP = XP # (float) experience que le joueur recevra à la fin de l'intervfention : change au court de celle-ci 
    self.timer = time ## (float) nombre de secondes avant la fin de l'intervention
    
  # accepter l'intervention     
   
    def accept(self): # accepter une intervention 
      
    def refuse (self): # refuser une intervention
      
    def transmit(self, service): # donner l'ordre d'intervention a un autre service
      ## service : string = { SAMU, POLICE, ... }
      
    def defer(self):  # remettre a plus tard une intervention
      
    def close(self): # fini l'intervention ou l'annule 


      

## Objet de type 'chemin' pour décrire un passage

class chemin :
  "Represente un chemin / route"
  
  def __init__ (self, x1, y1, x2, y2):
    ## (float) x1, y1, x2, y2
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
      
      
      
############ FONCTIONS GLOBALES #########

def find_paths (x1, x2, y1, y2) : # Trouve le chemin le plus court pour aller du couple (x1;y1) au couple (x2;y2) 
  # (float) x1, x2, y1, y2 
  return # retourne un tableau contenant des object de type 'chemin' (celui que l'on doit suivre)  
  
def find_next_path (x, y) : ### Trouve dans le tableau généré par 'find_paths' le prochain chemin (morceau de route) à emprunter pour aller aux coordonnées x et y
  ### (float) x, y
  return ### retourne un objet de type 'chemin' du tableau généré par 'find_paths' (le prochain à suivre)
  
def update (DT) : # bouge les vehicules (raffraichit leur position) et actualise les timers des interventions en fonction de DT 
  ##DeltaTime = DT (float) : temps en millisecondes depuis la dernière update
  
def generate_intervention () : ### génère un objet de type 'intervention' aléatoirement
  return ## retourne un objet de type 'intervention'

  
#################################### END ####################################
