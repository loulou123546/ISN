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



depanneuse1 = vehicles(001, 'camion accidents', 'DEPANNEUSE1', 'SERVICE', ['AVP','DIV'], 'depanneuse1.png')
depanneuse2 = vehicles(002, 'camion accidents', 'DEPANNEUSE2', 'SERVICE', ['AVP','DIV'], 'depanneuse2.png' )
patrouilleur = vehicles(003, 'camionette balisage', 'PATROUILLEUR', 'SERVICE', ['DIV'], 'patrouilleur2.png')
umh = vehicles(004, 'ambulance', 'UMH', 'SAMU', ['SAP'], 'UMH1.png')
vsav1 = vehicles(005, 'ambulance', 'VSAV1', 'POMPIER', ['SAP'], 'VSAV1.png')
vsav2 = vehicles(006,'ambulance', 'VSAV2''POMPIER', ['SAP'], 'VSAV2.png')
vsr = vehicles(007, 'camion accidents', 'VSR', 'POMPIER', ['AVP'], 'VSR1.png')
fptsr = vehicles(008, ['camion accidents','FPTSR', 'camion incendie'], 'FPTSR', 'POMPIER', ['AVP','INC','DIV'], 'FPTSR1.png')
vlpompier = vehicles(009, 'voiture', 'VLPOMPIER', 'POMPIER', ['DIV'], 'VL_pompier1.png')
vlpoliceE = vehicles(011, 'voiture', 'VLPOLICE', 'POLICE', ['DIV','CRM'], 'VL_police1.png')
pcm = vehicules(013, 'camion commande', 'PCM', 'POLICE', ['DIV'], 'PCM1.png')
dragon = vehicles(015, 'helicoptere' , 'DRAGON', 'POMPIER', ['DIV','SAP'], 'dragon_avec_rotor1.png')
gaitan = vehicles(016, 'helicoptere', 'GAITAN', 'POLICE', ['DIV'], 'gaitan_avec_rotor1.png')
victor = vehicles(017, 'airambulance', 'VICTOR', 'SAMU', ['SAP'], 'victor_avec_rotor.png')
vlu = vehicles(018, 'voiture banalisee', 'VLU', 'POLICE', ['DIV','CRM'], 'undercover1.png')
ccf = vehicles(019, 'camion incendie', 'CCF', 'POMPIER', ['INC'], 'CCF1.png')
epa = vehicles(020, 'camion incendie', 'EPA', 'POMPIER',['DIV', ['INC'], 'EPA1.png')
fpt = vehicles(021, 'camion incendie', 'FPT', 'POMPIER', ['DIV','INC'], 'FPT1.png')
vlm = vehicles(022, 'voiture', 'VLM', 'SAMU', ['SAP'], 'VLM1.png')
vtu = vehicles(023, 'camionette', 'VTU', 'POMPIER', ['DIV'], 'VTU1.png')
ccgc = vehicles(024, 'camion incendie', 'CCGC', 'POMPIER', ['DIV'], 'CCGC1.png')
bri = vehicles(025, 'voiture', 'BRI', 'POLICE', ['DIV'], 'BRI_police1.png')
ambulance = vehicles(026, 'ambulance', 'AMBULANCE', 'SERVICE', ['SAP'], 'ambu_privé1.png')
gerdf = vehicles(027, 'voiture', 'GERDF', 'SERVICE', ['DIV'], 'VL_GRDF1.png')
nacelle = vehicles(029, 'camion electricite', 'NACELLE', 'SERVICE', ['DIV'], 'ERDF2.png')
fourgon = vehicles(030, 'fourgon transport prisonnier', 'FOURGON', 'POLICE', ['ARR'], 'fourgon_prisonnier2.png')
swat = vehicles(031, 'fourgon blinde', 'SWAT', 'POLICE', ['ARR','CRM'], 'SWAT_team.png')
nrbc = vehicles(032, 'camion chimique', 'NRBC', 'POMPIER', ['DIV'], 'NRBC1.png')

def teleport (self, x, y): ### deplace le vehicule instantanément aux coordonnées x et y
  ## (float) x, y
    
  
def move (self, x, y): # déplace le vehicule en fonction des coordonnees x et y
  ## (float) x, y