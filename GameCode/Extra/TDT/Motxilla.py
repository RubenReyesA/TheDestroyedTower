# -*- coding: utf-8 -*-


class Motxilla():
    
    def __init__(self):
        self.m_nom="Motxilla"
        self.m_dict_obj={}
    
    
    def AddtoMotxilla(self, c, user):
        self.m_dict_obj[c.obj_nom]=c
        user.options["Mirar per la finestra"]=self.options["Mirar per la finestra2"]
        user.options["Sortir al balco"]=self.options["Sortir al balco2"]
        user.options["Anar a la porta - Hab1"]=self.options["Anar a la porta - Hab12"]
    
    def PrintMotxilla(self):
        cadena= ""
        for key in self.m_dict_obj.keys():

            cadena += key +" --> 1\n"
    
        return cadena
    
    