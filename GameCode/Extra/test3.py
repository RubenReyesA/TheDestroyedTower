# -*- coding: utf-8 -*-
import copy as cp
import string

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

ranquing=[]


file=open("dialegs.txt","r")
    
dialog={}
teclats={}
    
for line in file.readlines():
    if(line!="\n"):
            lista=line.strip().split("___")
            command=lista.pop(0)
            dialog[command]=cp.copy(lista)
            del(lista)
file.close()

file=open("teclats.txt","r")
        
        
for line in file.readlines():
       if(line!="\n"):
          lista=line.strip().split("___")
          command=lista.pop(0)
          teclats[command]=[lista[i:i+1] for i in range(0, len(lista))]
          del(lista)
file.close()
    
def cargar_ranquing():
    file=open("ranquing.txt","r")
            
    for line in file.readlines():
           if(line!="\n"):
              lista=line.split("___")
              lista[2]=int(lista[2])
              ranquing.append(lista)
             
    file.close()

def guardar_ranquing():
    file=open("ranquing.txt","w")
    
    for item in ranquing:
        file.write(item[0]+"___"+item[1]+"___"+str(item[2])+"\n")
    
    file.close()
    
    ranquing.sort(key=lambda ranquing: ranquing[2])
    ranquing.reverse()
    
def generar_teclat(x):
    a=ReplyKeyboardMarkup(x,one_time_keyboard=True)
    return a
    
    
    
    
    
    
    