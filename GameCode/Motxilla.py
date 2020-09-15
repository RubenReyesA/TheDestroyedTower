# -*- coding: utf-8 -*-


class Motxilla():
    
    def __init__(self):
        self.m_nom="Motxilla"
        self.m_dict_obj={}
    
    
    def AddtoMotxilla(self, c, user):
        self.m_dict_obj.update(c)

    
    def PrintMotxilla(self):
        cadena= ""
        for key in self.m_dict_obj.keys():

            cadena += key +" --> 1\n"
    
        return cadena
    
    