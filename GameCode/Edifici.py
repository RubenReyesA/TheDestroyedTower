# -*- coding: utf-8 -*-

import Planta as planta
import Porta as porta
import Habitacio as hab
import Finestra as fin
import Objecte as obj

class Edifici():
    
    def __init__(self, nom,e_plantes=None):
        self.e_nom=nom
        self._init_map(e_plantes)
        
    def _init_map(self, e_plantes):
        
        """ Creació d'objectes per interactuar"""
        finestra=fin.Finestra("Finestra")
        targeta_daurada=obj.TargetaClau("Targeta Daurada",False)
        armari=obj.Armari("Armari")
        CPD=obj.CPD("CPD",False)
        i3D=obj.Impressora3di("Impressora 3Di",False)
        llit=obj.Llit("Llit")
        cadira=obj.Cadira("Cadira")
        taula=obj.Taula("Taula")
        indv=obj.Individu("Guarda")
        
        pp=porta.Porta("Porta Principal")
        p1=porta.Porta("Porta - Hab1")
        p2=porta.Porta("Porta - Hab2")
        p3=porta.Porta("Porta - Hab3")
        p4=porta.Porta("Porta - Hab4")
        p5=porta.Porta("Porta - Hab5")
        
        hab1=hab.Habitacio("Habitació 1",p1,finestra)
        p1.set_hab(hab1)
        hab2=hab.Habitacio("Habitació 2",p2)
        hab2.h_dict_obj[llit.obj_nom]=llit
        hab2.h_dict_obj[cadira.obj_nom]=cadira
        hab2.h_dict_obj[taula.obj_nom]=taula
        p2.set_hab(hab2)
        hab3=hab.Habitacio("Habitació 3",p3)
        hab3.h_dict_obj[targeta_daurada.obj_nom]=targeta_daurada
        p3.set_hab(hab3)
        hab4=hab.Habitacio("Habitació 4",p4)
        hab4.h_dict_obj[armari.obj_nom]=armari
        p4.set_hab(hab4)
        hab5=hab.Habitacio("Habitació 5",p5)
        hab5.h_dict_obj[CPD.obj_nom]=CPD
        hab5.h_dict_obj[i3D.obj_nom]=i3D
        p5.set_hab(hab5)
        
        
        portes1=[pp]
        portes2=[p1,p2]
        portes3=[p3]
        portes4=[p4,p5]
        
        plantes={}
        
        plantes["Planta 1"]=planta.Planta("Planta 1",portes1,True,False)
        plantes["Planta 2"]=planta.Planta("Planta 2",portes2,True,False)
        plantes["Planta 3"]=planta.Planta("Planta 3",portes3,True,False,indv)
        plantes["Planta 4"]=planta.Planta("Planta 4",portes4,True,False)
        
        self.e_plantes=plantes