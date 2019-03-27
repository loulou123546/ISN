class vehicles :
    "vehicules de la caserne"
  
def __init__(self, ID, typ, name, vhc_cat, capacites, skin):
  # (int) ID - (string) typ - (string) name 
  self.x = 0
  self.y = 0
  self.type = typ ## (string) = { camion incendie, ambulance... }
  self.ID = ID ## (int) ID unique = { 001, 002, 003, ... }
  self.hidden = True ### (bool) afficher le vehicule: True = cache, False = affiche
  self.name = name ### (string) Nom complet du vehicule
  self.vhc_cat = vhc_cat ## (string) vhc_cat = { VSAV, FPT, ... }
  self.capacites = capacites ## capacites [] (string) = { SAP, INC, DIV, ... }
  self.skin = skin ## picture



DEPANNEUSE1 = vehicles(001, 'camion accidents', 'DEPANNEUSE1', 'SERVICE', ['AVP','DIV'], 'depanneuse1.png')
DEPANNEUSE2 = vehicles(002, 'camion accidents', 'DEPANNEUSE2', 'SERVICE', ['AVP','DIV'], 'depanneuse2.png' )
PATROUILLEUR = vehicles(003, 'camionette balisage', 'PATROUILLEUR', 'SERVICE', ['DIV'], 'patrouilleur2.png')
UMH = vehicles(004, 'ambulance', 'UMH', 'SAMU', ['SAP'], 'UMH1.png')
VSAV1 = vehicles(005, 'ambulance', 'VSAV1', 'POMPIER', ['SAP'], 'VSAV1.png')
VSAV2 = vehicles(006,'ambulance', 'VSAV2''POMPIER', ['SAP'], 'VSAV2.png')
VSR = vehicles(007, 'camion accidents', 'VSR', 'POMPIER', ['AVP'], 'VSR1.png')
FPTSR = vehicles(008, ['camion accidents','FPTSR', 'camion incendie'], 'FPTSR', 'POMPIER', ['AVP','INC','DIV'], 'FPTSR1.png')
VLPOMPIER = vehicles(009, 'voiture', 'VLPOMPIER', 'POMPIER', ['DIV'], 'VL_pompier1.png')
VLPOLICE = vehicles(011, 'voiture', 'VLPOLICE', 'POLICE', ['DIV','CRM'], 'VL_police1.png')
PCM = vehicules(013, 'camion commande', 'PCM', 'POLICE', ['DIV'], 'PCM1.png')
DRAGON = vehicles(015, 'helicoptere' , 'DRAGON', 'POMPIER', ['DIV','SAP'], 'dragon_avec_rotor1.png')
GAITAN = vehicles(016, 'helicoptere', 'GAITAN', 'POLICE', ['DIV'], 'gaitan_avec_rotor1.png')
VICTOR = vehicles(017, 'airambulance', 'VICTOR', 'SAMU', ['SAP'], 'victor_avec_rotor.png')
VLU = vehicles(018, 'voiture banalisee', 'VLU', 'POLICE', ['DIV','CRM'], 'undercover1.png')
CCF = vehicles(019, 'camion incendie', 'CCF', 'POMPIER', ['INC'], 'CCF1.png')
EPA = vehicles(020, 'camion incendie', 'EPA', 'POMPIER',['DIV', ['INC'], 'EPA1.png')
FPT = vehicles(021, 'camion incendie', 'FPT', 'POMPIER', ['DIV','INC'], 'FPT1.png')
VLM = vehicles(022, 'voiture', 'VLM', 'SAMU', ['SAP'], 'VLM1.png')
VTU = vehicles(023, 'camionette', 'VTU', 'POMPIER', ['DIV'], 'VTU1.png')
CCGC = vehicles(024, 'camion incendie', 'CCGC', 'POMPIER', ['DIV'], 'CCGC1.png')
BRI = vehicles(025, 'voiture', 'BRI', 'POLICE', ['DIV'], 'BRI_police1.png')
AMBULANCE = vehicles(026, 'ambulance', 'AMBULANCE', 'SERVICE', ['SAP'], 'ambu_privé1.png')
GERDF = vehicles(027, 'voiture', 'GERDF', 'SERVICE', ['DIV'], 'VL_GRDF1.png')
NACELLE = vehicles(029, 'camion electricite', 'NACELLE', 'SERVICE', ['DIV'], 'ERDF2.png')
FOURGON = vehicles(030, 'fourgon transport prisonnier', 'FOURGON', 'POLICE', ['ARR'], 'fourgon_prisonnier2.png')
SWAT = vehicles(031, 'fourgon blinde', 'SWAT', 'POLICE', ['ARR','CRM'], 'SWAT_team.png')
NRBC = vehicles(032, 'camion chimique', 'NRBC', 'POMPIER', ['DIV'], 'NRBC1.png')

def teleport (self, x, y): ### deplace le vehicule instantanément aux coordonnées x et y
  ## (float) x, y
    
  
def move (self, x, y): # déplace le vehicule en fonction des coordonnees x et y
  ## (float) x, y