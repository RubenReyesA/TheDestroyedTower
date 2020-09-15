# -*- coding: utf-8 -*-

class Porta():
    
    def __init__(self,nom):
        self.pt_nom=nom
        self.pt_oberta=False
        
    def obrir_porta(self):
        self.pt_oberta=True
        
    def tancar_porta(self):
        self.pt_oberta=False