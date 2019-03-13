class intervention :
  "Intervention en cours ou fini"
  
    def __init__ (self, ID, typ, x, y, XP, time):
    ## (int) ID   -   (string) typ   -   (float) x   -   (float) y   -   (float) XP   -   (float) time 
        self.x = x
        self.y = y
        self.typ = typ ## (string) type = { INC, SAP, DIV, ... }
        self.ID = ID ### (int) ID unique = { 001, 002, 003, ... }
        self.fini = False # (bool) intervention non terminee 
        self.XPmaxi = XP # (float) experience maximale a obtenir lors de l'intervention
        self.XP = XP # (float) experience que le joueur recevra à la fin de l'intervfention : change au court de celle-ci 
        self.timer = time ## (float) nombre de secondes avant la fin de l'intervention

    def open_menu(self):


    def accept(self): # accepter une intervention 
        

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
            if self.typ = 'AVP' or self.typ == 'SAP' or self.typ == 'REN':
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
      



    def close(self): # fini l'intervention ou l'annule 


# typ = INC(=incendie), SAP(=secours à personne), AVP(=accident de la voie publique), DIV(=divers), CRM(=crime), ARR(=arrestation), REN(=renforts)
