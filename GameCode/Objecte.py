# -*- coding: utf-8 -*-

class Objecte:
    def __init__(self, nom):
        self.obj_nom = nom
    
class Contenidor(Objecte):
    def __init__(self, nom,d={}):
        self.obj_nom = nom
        self.dict_obj=d
        
class Contingut(Objecte):
    def __init__(self, nom,agafat):
        self.obj_nom = nom
        self.obj_agafat=agafat
        
        
    def agafar_objecte(self):
        self.obj_agafat=True


class Peluix(Contingut):
    pass

class Llit(Contenidor):
    def __init__(self,nom):
        peluix={"Peluix Pokemon":Peluix("Peluix Pokemon",False)}
        Contenidor.__init__(self,nom,peluix)
        
class Soga(Contingut):
    pass
        
class Cadira(Contenidor):
    def __init__(self,nom):
        soga={"Soga":Soga("Soga",False)}
        Contenidor.__init__(self,nom,soga)

class Pila(Contingut):
    pass

class Llanterna(Contenidor):
    def __init__(self,nom,agafat):
        Contenidor.__init__(self,nom)
        self.obj_agafat=agafat
        
    def agafar_llanterna(self):
        self.obj_agafat=True
        
    def utilitzar_piles(self,pila):
        self.dict_obj["Pila"]=pila
        
class Taula(Contenidor):
   def __init__(self,nom):
        llanterna={"Llanterna":Llanterna("Llanterna",False)}
        Contenidor.__init__(self,nom,llanterna)

class TargetaClau(Contingut):
    pass

class Individu(Contenidor):
    def __init__(self,nom):
        targeta={"Targeta Guarda":TargetaClau("Targeta Guarda",False)}
        Contenidor.__init__(self,nom,targeta)
        
class Material3Di(Contingut):
    pass

class Impressora3di(Contenidor):
    def __init__(self,nom,c):
        material={"Material 3Di":Material3Di("Material3Di",False),"Targeta Mestra":TargetaClau("Targeta Mestra",False)}
        Contenidor.__init__(self,nom,material)
        self.impressora_carregada=c
    
    def carregar_impressora(self,state):
        self.impressora_carregada=state
        
    def imprimir_tarja_mestra(self):
        self.dict_obj["Targeta Mestra"].agafar_objecte()

class Tigreton(Contingut):
    pass
class Beer(Contingut):
    pass
class FontAlimentacio(Contingut):
    pass

class Armari(Contenidor):
    def __init__(self,nom):
        d={"Pila":Pila("Pila",False),"Tigretón":Tigreton("Tigretón",False),"Beer":Beer("Beer",False),
           "Font d'Alimentació":FontAlimentacio("Font d'Alimentació",False)}
        Contenidor.__init__(self,nom,d)

    def retirar_objectes(self): 
        self.dict_obj=None

class CPD(Contenidor):
    def __init__(self,nom,state):
        Contenidor.__init__(self,nom)
        self.canvi_font=state
    
    def canviar_font(self,font):
        self.dict_obj["Font d'Alimentació"]=font
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    