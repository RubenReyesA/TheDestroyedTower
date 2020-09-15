# -*- coding: utf-8 -*-

import traceback

class Option:
    
    def __init__(self, lista_texto, lista_opciones,lista_modf,time):
        self.texto_enviar=lista_texto
        self.lista_opciones = lista_opciones
        self.lista_modificar=lista_modf
        self.time=time
        
    def realizar_modf(self, user,to_send,to_type):

        try:       
            for item in self.lista_modificar:
                
                if ".txt" in item:
                    exec(compile(open(item, "rb").read(), item, 'exec'))
                else:
                    exec(item)
            
            if(user.u_timer.t_timer==0):
                to_send=user.options["TimeOut"].texto_enviar
                to_type=user.options["TimeOut"].lista_opciones
            
            return to_send, to_type
        except Exception:
            traceback.print_exc()