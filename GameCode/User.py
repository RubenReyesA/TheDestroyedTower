# -*- coding: utf-8 -*-

import Timer as t2
import Option as t4
import copy as cp
import Habitacio as hab
import Porta as porta
import Finestra as fin
import Motxilla as mot
import Edifici as edif

class User:
    
    def __init__(self,nom,chatID,options=None,u_edifici=None):
        self.u_nom=nom
        self.u_chatID=chatID
        self.u_timer=t2.Timer("Timer1",1200)
        self._init_options(options)
        self.u_motxilla=mot.Motxilla()
        self.u_edifici=edif.Edifici("The Destroyed Tower")
        
    def _init_options(self, options):
        
      options={}
      file=open("dc.txt","r")
    
      dialog={}
    
      for line in file.readlines():
        if(line!="\n"):
                lista=line.strip().split("___")
                command=lista.pop(0)
                for index,item in enumerate(lista):
                    lista[index]=item.split(':')
                dialog[command]=cp.copy(lista)
                del(lista)
      file.close()
      
      teclats={}
      
      file=open("tc.txt","r")
        
        
      for line in file.readlines():
           if(line!="\n"):
              lista=line.strip().split("___")
              command=lista.pop(0)
              teclats[command]=[lista[i:i+1] for i in range(0, len(lista))]
              del(lista)
      file.close()
      
      rm={}
      
      file=open("rm.txt","r")
        
        
      for line in file.readlines():
           if(line!="\n"):
              lista=line.strip().split("___")
              command=lista.pop(0)
              rm[command]=cp.copy(lista)
              del(lista)
      file.close()
      
      for key in dialog.keys():
          options[key]=t4.Option(dialog[key],
                 teclats[key],
                 rm[key],5)
     
      self.options = options
      