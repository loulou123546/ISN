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

  def teleport (self, x, y): ### deplace le vehicule instantanément aux coordonnées x et y
    ## (float) x, y
    
  
  def move (self, x, y): # déplace le vehicule en fonction des coordonnees x et y
    ## (float) x, y

DEPANNEUSE_1 = vehicles(001, 'camion accidents', 'depanneuse_1', 'SERVICE', ['AVP','DIV'], 'depanneuse1.png')
DEPANNEUSE_2 = vehicles(002, 'camion accidents', 'depanneuse_2', 'SERVICE', ['AVP','DIV'], 'depanneuse2.png' )'
PATROUILLEUR = vehicles(003, 'camionette balisage', 'patrouilleur', 'SERVICE', ['DIV'], 'patrouilleur2.png')
UMH = vehicles(004, 'ambulance', 'UMH', 'SAMU', ['SAP'], 'UMH1.png')
VSAV_1 = vehicles(005, 'ambulance', 'VSAV_1', 'POMPIER', ['SAP'], 'VSAV1.png')
VSAV_2 = vehicles(006,'ambulance', 'VSAV_2''POMPIER', ['SAP'], 'VSAV2.png')
VSR = vehicles(007, 'camion accidents', 'VSR', 'POMPIER', ['AVP'], 'VSR1.png')
FPTSR = vehicles(008, ['camion accidents', 'camion incendie'], 'FPTSR', 'POMPIER', ['AVP','INC','DIV'], 'FPTSR1.png')
VL_POMPIER = vehicles(009, 'voiture', 'VL_pompier', 'POMPIER', ['DIV'], 'VL_pompier1.png')
VLHR_POMPIER = vehicles(010, 'voiture', 'VLHR_pompier', 'POMPIER', ['DIV'], 'VLHR_pompier1.png')
VL_POLICE = vehicles(011, 'voiture', 'VL_police', 'POLICE', ['DIV','CRM'], 'VL_police1.png')
VLHR_POLICE = vehicles(012, 'voiture', 'VLHR_police', 'POLICE', ['DIV','CRM'], 'VLHR_police1.png')
PCM_1 = vehicules(013, 'camion commande', 'PCM_1', 'POLICE', ['DIV'], 'PCM1.png')
PCM_2 = vehicules(014, 'camion commande', 'PCM_2', 'POMPIER', ['DIV'], 'PCM2.png')
DRAGON = vehicles(015, 'helicoptere' , 'Dragon', 'POMPIER', ['DIV','SAP'], 'dragon_avec_rotor1.png')
GAITAN = vehicles(016, 'helicoptere', 'Gaitan', 'POLICE', ['DIV'], 'gaitan_avec_rotor1.png')
VICTOR = vehicles(017, 'airambulance', 'victor', 'SAMU', ['SAP'], 'victor_avec_rotor.png')
VLU = vehicles(018, 'voiture banalisee', 'VLU', 'POLICE', ['DIV','CRM'], 'undercover1.png')
CCF = vehicles(019, 'camion incendie', 'CCF', 'POMPIER', ['INC'], 'CCF1.png')
EPA = vehicles(020, 'camion incendie', 'POMPIER',['DIV', ['INC'], 'EPA1.png')
FPT = vehicles(021, 'camion incendie', 'FPT', 'POMPIER', ['DIV','INC'], 'FPT1.png')
VLM = vehicles(022, 'voiture', 'VLM', 'SAMU', ['SAP'], 'VLM1.png')
VTU = vehicles(023, 'camionette', 'VTU', 'POMPIER', ['DIV'], 'VTU1.png')
CCGC = vehicles(024, 'camion incendie', 'CCGC', 'POMPIER', ['DIV'], 'CCGC1.png')
BRI = vehicles(025, 'voiture', 'BRI', 'POLICE', ['DIV'], 'BRI_police1.png')
AMBULANCE = vehicles(026, 'ambulance', 'ambulance privee', 'SERVICE', ['SAP'], 'ambu_privé1.png')
GRDF = vehicles(027, 'voiture', 'GRDF', 'SERVICE', ['DIV'], 'VL_GRDF1.png')
ERDF = vehicles(028, 'voiture', 'ERDF', 'SERVICE', ['DIV'], 'VL_GRDF1.png')
NACELLE = vehicles(029, 'camion electricite', 'camion nacelle ERDF', 'SERVICE', ['DIV'], 'ERDF2.png')
FOURGON = vehicles(030, 'fourgon transport prisonnier', 'prisonner', 'POLICE', ['ARR'], 'fourgon_prisonnier2.png')
SWAT = vehicles(031, 'fourgon blinde', 'SWAT', 'POLICE', ['ARR','CRM'], 'SWAT_team.png')
NRBC = vehicles(032, 'camion chimique', 'NRBC', 'POMPIER', ['DIV'], 'NRBC1.png')