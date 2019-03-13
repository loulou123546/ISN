class vehicles_skills :
  "capacites des vehicules"
  
    def __init__(self, vhc_cat, capacites) :
    ## (string) vhc_cat = { VSAV, FPT, ... }    -   capacites [] (string) = { 'SAP', 'INC', 'DIV', ... }
        
        self.vhc_cat = vhc_cat ## (string) vhc_cat = { VSAV, FPT, ... }
        self.capacites = capacites ## capacites [] (string) = { 'SAP', 'INC', 'DIV', ... }


# liste véhicules

DEPANNEUSE_1 = vehicles_skills('SERVICE',['AVP','DIV'])
DEPANNEUSE_2 = vehicles_skills('SERVICE',['AVP','DIV'])
PATROUILLEUR = vehicles_skills('SERVICE','DIV')
UMH = vehicles_skills('SAMU','SAP')
VSAV_1 = vehicles_skills('POMPIER','SAP')
VSAV_2 = vehicles_skills('POMPIER','SAP')
VSR = vehicles_skills('POMPIER','AVP')
FPTSR = vehicles_skills('POMPIER',['AVP','INC','DIV'])
VL_POMPIER = vehicles_skills('POMPIER','DIV')
VLHR_POMPIER = vehicles_skills('POMPIER','DIV')
VL_POLICE = vehicles_skills('POLICE',['DIV','CRM'])
VLHR_POLICE = vehicles_skills('POLICE',['DIV','CRM'])
PCM_1 = vehicules_skills('POLICE','DIV')
PCM_2 = vehicules_skills('POMPIER','DIV')
DRAGON = vehicles_skills('POMPIER',['DIV','SAP'])
GAITAN = vehicles_skills('POLICE','DIV')
VICTOR = vehicles_skills('SAMU','SAP')
VLU = vehicles_skills('POLICE',['DIV','CRM'])
CCF = vehicles_skills('POMPIER','INC')
EPA = vehicles_skills('POMPIER',['DIV','INC'])
FPT = vehicles_skills('POMPIER',['DIV','INC'])
VLM = vehicles_skills('SAMU','SAP')
VTU = vehicles_skills('POMPIER','DIV')
CCGC = vehicles_skills('POMPIER','DIV')
BRI = vehicles_skills('POLICE','DIV')
AMBULANCE = vehicles_skills('SERVICE','SAP')
GRDF = vehicles_skills('SERVICE','DIV')
ERDF = vehicles_skills('SERVICE','DIV')
NACELLE = vehicles_skills('SERVICE','DIV')
FOURGON = vehicles_skills('POLICE','ARR')
SWAT = vehicles_skills('POLICE',['ARR','CRM'])
NRBC = vehicles_skills('POMPIER','DIV')
