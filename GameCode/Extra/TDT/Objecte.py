# -*- coding: utf-8 -*-

class Objecte:
    
    def __init__(self, nom,a):
        self.obj_nom = nom
        self.obj_agafat=a
    
class Contenidor(Objecte):
    '''Clase que incluye actividades de los mamíferos.'''
    
    def reproduccion(self):
        '''Es la implementación de la interfaz reproduccion de la superclase.'''
        print('Toma un cachorro.')
    
    def amamanta(self):
        print('Toma un vaso de leche.')
        
class Contingut(Objecte):
    
    def agafar_objecte(self):
        self.obj_agafat=True
