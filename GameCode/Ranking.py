# -*- coding: utf-8 -*-

import datetime

class Ranking():
    
    def __init__(self,nom,dictionary=None):
        self.r_Nom=nom
        self.r_Ranking=dictionary
    
    def ReadTXT(self):
        self.r_Ranking=[]
        file=open("ranquing.txt","r")
            
        for line in file.readlines():
           if(line!="\n"):
              lista=line.split("___")
              lista[1]=int(lista[1])
              self.r_Ranking.append(lista)
             
        file.close()
        
        self.r_Ranking.sort(key=lambda ranquing: ranquing[1])
        self.r_Ranking.reverse()
        
    def WriteTXT(self):
        file=open("ranquing.txt","w")
    
        for item in self.r_Ranking:
            file.write(item[0]+"___"+str(item[1])+"\n")
    
        file.close()
        
    def FiveFirstRanking(self):
        
        cadena=""
        
        for x in range(0,5):
            cadena += self.r_Ranking[x][0] +" --> "+str(datetime.timedelta(seconds=self.r_Ranking[x][1]))[2:]+"\n"
                
        return cadena
                
    def printRanking(self,username=None):
        cadena=""
        i=0
        if(username!=None):
            for x in range(len(self.r_Ranking)):
                i+=1
                if((self.r_Ranking[x][0])!=username):
                    cadena += str(i)+".- "+self.r_Ranking[x][0] +" --> "+str(datetime.timedelta(seconds=self.r_Ranking[x][1]))[2:]+"\n"
                else:
                    cadena += str(i)+".- *_' "+self.r_Ranking[x][0] +" --> "+str(datetime.timedelta(seconds=self.r_Ranking[x][1]))[2:]+"'_*\n"
        else:
            for x in range(len(self.r_Ranking)):
                i+=1
                cadena += str(i)+".- "+self.r_Ranking[x][0] +" --> "+str(datetime.timedelta(seconds=self.r_Ranking[x][1]))[2:]+"\n"
         
        return cadena
    
    def AddtoRanking(self, u):
        lista=[]
        lista.append(u.u_nom)
        lista.append(u.u_timer.t_timer)
        self.r_Ranking.append(lista)
        self.r_Ranking.sort(key=lambda ranquing: ranquing[1])
        self.r_Ranking.reverse()
        self.WriteTXT()