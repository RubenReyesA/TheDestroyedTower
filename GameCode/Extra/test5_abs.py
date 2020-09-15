# -*- coding: utf-8 -*-

import copy as cp
import test4 as t4

options={}
file=open("dc.txt","r")

a=2
dialog={}

if(a==2):
    
      for line in file.readlines():
        if(line!="\n"):
                lista=line.strip().split("___")
                command=lista.pop(0)
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
      
      for llave, text, option, rm in zip(dialog.keys(),dialog.values(),teclats.values(),rm.values()):

          myopt=t4.Option(text,option,rm)
          options[llave]=cp.deepcopy(myopt)