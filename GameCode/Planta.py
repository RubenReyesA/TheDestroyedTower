# -*- coding: utf-8 -*-

import Porta as porta
import copy as cp

class Planta():
    
    def __init__(self, nom,portes,ad,et,indv=None):
        self.p_nom=nom
        self._init_portes(portes)
        self.ascensor_disponible=ad
        self.escales_trobades=et
        self.individu=indv
    
    def _init_portes(self, portes):
        
        p_portes={}
        
        for item in portes:
            p_portes[item.pt_nom]=cp.deepcopy(item)
        
        self.p_portes=p_portes
        
    def activar_ascensor(self):
        self.ascensor_disponible=True
    
    def desactivar_ascensor(self):
        self.ascensor_disponible=False
    
    def marcar_escales_trobades(self):
        self.escales_trobades=True