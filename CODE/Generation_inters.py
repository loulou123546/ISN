import random

def generate_inters() :
    
    inters = ['accident routier VL', 'animal coince', "arrestation d'un suspect", 'arret cardique', 'blessure en montage', 'blessure/malaise', 'cambriolage', 'convoi', 'feu de foret', 'feu en ville', 'feu en zone maritime (port)', 'fuite de gaz', 'incident chimique/nucleaire', 'incident ligne EDF', 'personnne disparue', 'tentative de meurtre', 'voiture mal stationee', 'zone de controle radar', 'renfort','accident routier PL']
    renforts = ['police', 'incendie', 'medical', 'transport', 'escorte', 'intervention1', 'electrique ou gaz', 'prisonniers', 'depannage VL','depannage PL', 'balisage']
    intervention1 = []
    intervention2 = []
    #vehicules = ['BRI', 'CCF', 'CCGC', 'DRAGON', 'EPA', 'ERDF', 'FPT', 'FPTSR', 'GRDF', 'GAITAN', 'NRBC', 'PCM', 'SAMU', 'SWAT', 'VLPOMPIER', 'VLM', 'VLU', 'VLPOLICE', 'VSAV, 'VSR', 'VTU', 'AMBULANCE', 'NACELLE', 'DEPANNEUSE1', 'DEPANNEUSE2', 'PATROUILLEUR', 'FOURGON','UMH', 'VICTOR']
    #typ_INC = ['CCF', 'EPA', 'FPT', 'FPTSR', 'VSAV', 'CCGC']
    #typ_SAP =['PCM', 'VLPOMPIER', 'VSAV', 'VLM', 'DRAGON', 'GAITAN' , 'UMH', 'VICTOR', 'AMBULANCE', 'SAMU']
    #typ_AVP =['DEPANNEUSE1', 'DEPANNEUSE2', 'PATROUILLEUR', 'UMH', 'VSAV', 'VSR', 'FPTSR', 'VLPOLICE']
    #typ_DIV =['VLPOLICE', 'DEPANNEUSE1', 'DEPANNEUSE2', 'VTU', 'BRI', 'VLU', 'GRDF', 'FPT', 'FPTSR', 'ERDF', 'NACELLE', 'NRBC', 'VSAV', 'VSAV', 'UMH' ]
    #typ_ARR =['VLPOLICE', 'FOURGON', 'SWAT']
    #typ_REN =['VLPOLICE', 'VLPOMPIER', 'FPT', 'FPTSR', 'CCF', 'UMH', 'VLM', 'DRAGON', 'VICTOR', 'SWAT', 'ERDF', 'GRDF', 'FOURGON', 'DEPANNEUSE1', 'DEPANNEUSE2', 'PATROUILLEUR']
    #typ_CRM =['VLPOLICE', 'UMH', 'VSAV', 'VSAV', 'VLU']

    numero_inter = random.randint(0, (len (inters)-1))
    numero_renfort = random.randint(0, (len(renforts)-1))

    if numero_inter == 0: #accident routier VL
        intervention1.append(inters[0])
        intervention1.append('DEPANNEUSE1')
        intervention1.append('PATROUILLEUR')
        intervention1.append('UMH')
        intervention1.append('VSAV1') 
        intervention1.append('VSR')
        intervention1.append('FPTSR')
        intervention1.append('VLPOLICE')
        intervention2 = intervention1

    if numero_inter == 1: #animal coince
        intervention1.append(inters[1])
        intervention1.append('VTU')
        intervention2 = intervention1

    if numero_inter == 2: # arrestation d'un suspect
        intervention1.append(inters[2])
        intervention1.append('VLPOLICE')
        intervention1.append('VLPOLICE')
        intervention1.append('FOURGON')
        intervention1.append('SWAT')
        intervention2 = intervention1

    if numero_inter == 3: #arret cardiaque
        intervention1.append(inters[3])
        intervention1.append('VSAV')
        intervention1.append('UMH')
        intervention2 = intervention1

    if numero_inter == 4: # blessure en montage
        intervention1.append(inters[4])
        intervention1.append('VLM')
        intervention1.append('DRAGON')
        intervention1.append('VICTOR')
        intervention2 = intervention1

    if numero_inter == 5: # blessure/malaise
        intervention1.append(inters[5])
        intervention1.append('AMBULANCE')
        intervention1.append('VSAV')
        intervention1.append('SAMU')
        intervention2 = intervention1

    if numero_inter == 6: #cambiolage
        intervention1.append(inters[6])
        intervention1.append('VLPOLICE')
        intervention2 = intervention1

    if numero_inter == 7: #convoi
        intervention1.append(inters[7])
        intervention1.append('VLPOLICE')
        intervention1.append('VLPOLICE')
        intervention2 = intervention1

    if numero_inter == 8: #feu de foret
        intervention1.append(inters[8])
        intervention1.append('CCF')
        intervention2 = intervention1
    
    if numero_inter == 9: #feu en ville
        intervention1.append(inters[9])
        intervention1.append('EPA')
        intervention1.append('FPT')
        intervention1.append('VSAV')
        intervention2.append(inters[9])
        intervention2.append('EPA')
        intervention2.append('FPTSR')
        intervention2.append('VSAV')

    if numero_inter == 10: #feu en zone maritime (port)
        intervention1.append(inters[10])
        intervention1.append('FPT')
        intervention1.append('FPTSR')
        intervention1.append('VSAV')
        intervention1.append('CCGC')
        intervention2 = intervention1

    if numero_inter == 11: #fuite de gaz
        intervention1.append(inters[11])
        intervention1.append('GRDF')
        intervention1.append('FPT')
        intervention2.append(inters[11])
        intervention2.append('GRDF')
        intervention2.append('FPTSR')

    if numero_inter == 12: #incident chmique/nucleair
        intervention1.append(inters[12])
        intervention1.append('NRBC')
        intervention1.append('VSAV')
        intervention1.append('VSAV')
        intervention2.append(inters[12])
        intervention2.append('NRBC')
        intervention2.append('UMH')
        intervention2.append('UMH')
    
    if numero_inter == 13: #incident ligne EDF
        intervention1.append(inters[13])
        intervention1.append('ERDF')
        intervention1.append('NACELLE')
        intervention2 = intervention1
    
    if numero_inter == 14: #personne disparue
        intervention1.append(inters[14])
        intervention1.append('PCM')
        intervention1.append('VLPOMPIER')
        intervention1.append('VSAV')
        intervention1.append('DRAGON')
        intervention2.append(inters[14])
        intervention2.append('PCM')
        intervention2.append('VLPOMPIER')
        intervention2.append('GAITAN')
        intervention2.append('VLM')

    if numero_inter == 15: #tentative de meurtre
        intervention1.append(inters[15])
        intervention1.append('VLPOLICE')
        intervention1.append('UMH')
        intervention2.append(inters[15])
        intervention2.append('VLPOLICE')
        intervention2.append('VSAV')

    if numero_inter == 16: #voiture mal stationnee
        intervention1.append(inters[16])
        intervention1.append('VLPOLICE')
        intervention1.append('DEPANNEUSE1')
        intervention2 = intervention1

    if numero_inter == 17: #zone de control radar
        intervention1.append(inters[17])
        intervention1.append('BRI')
        intervention2.append(inters[17])
        intervention2.append('VLU')
    
    if numero_inter == 18: #renfort
        intervention1.append(inters[18])
        
        if numero_renfort == 0: #police
            intervention1.append(renforts[0])   
            intervention1.append('VLPOLICE')
            intervention2 = intervention1


        if numero_renfort == 1: #incendie
            intervention1.append(renforts[1])
            intervention1.append('FPT')
            intervention1.append('FPTSR')
            intervention1.append('CCF')
            intervention1.append('ABE')
            intervention2 = intervention1

        if numero_renfort == 2: #medical
            intervention1.append(renforts[2])
            intervention1.append('UMH')
            intervention1.append('VLM')
            intervention2 = intervention1

        if numero_renfort == 3: #transport
            intervention1.append(renforts[3])
            intervention1.append('DRAGON')
            intervention1.append('VICTOR')
            intervention2 = intervention1

        if numero_renfort == 4: #escorte
            intervention1.append(renforts[4])
            intervention1.append('VLPOLICE')
            intervention1.append('VLPOLICE')
            intervention2 = intervention1

 
        if numero_renfort == 5: #intervention1 
            intervention1.append(renforts[5])
            intervention1.append('SWAT')
            intervention2 = intervention1


        if numero_renfort == 6: #electrique ou gaz
            intervention1.append(renforts[6])
            intervention1.append('ERDF')
            intervention1.append('GRDF')
            intervention2 = intervention1

        if numero_renfort == 7: #prisonniers
            intervention1.append(renforts[7])
            intervention1.append('FOURGON')
            intervention2 = intervention1


        if numero_renfort == 8: #depannage VL
            intervention1.append(renforts[8])
            intervention1.append('DEPANNEUSE1')
            intervention2 = intervention1

        if numero_renfort == 9: #depannage PL
            intervention1.append(renforts[9])
            intervention1.append('depanneuse2')
            intervention2 = intervention1

        if numero_renfort == 10: #balisage
            intervention1.append(renforts[10])
            intervention1.append('PATROUILLEUR')
            intervention2 = intervention1

    if numero_inter == 19: #accident routier PL
        intervention1.append(inters[19])
        intervention1.append('DEPANNEUSE2')
        intervention1.append('PATROUILLEUR')
        intervention1.append('UMH')
        intervention1.append('VSAV')
        intervention1.append('VSR')
        intervention1.append('FPTSR')
        intervention1.append('VLPOLICE')
        intervention2.append(inters[19])
        intervention2.append('DEPANNEUSE2')
        intervention2.append('PATROUILLEUR')
        intervention2.append('UMH')
        intervention2.append('VSAV')
        intervention2.append('VSR')
        intervention2.append('FPTSR')
        intervention2.append('VLPOLICE')  



    return intervention1, intervention2

print(generate_inters())
    
