# -*- coding: utf-8 -*-

class Porta():
    
    def __init__(self,nom):
        self.pt_nom=nom
        self.pt_oberta=False
        self.pt_hab=None
    
    def set_hab(self, h):
        self.pt_hab=h
        
    def obrir_porta(self):
        self.pt_oberta=True
        
    def tancar_porta(self):
        self.pt_oberta=False