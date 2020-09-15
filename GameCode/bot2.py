#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#622283439:AAHA71tjo0yBz5oHWHhXRI_FlpVi7ISCZW0
"""
@author: ES_TEAM
"""
################################# IMPORTS ######################################
import pprint
import json
import codecs
import os
import copy
import time
import unicodedata

import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler)

import testbot2 as tb2
import User as t4
import Ranking as rank
######################### INFORMATION FOR APP ##################################

APP = 'destroyedtower'
APPNAME = 'TheDestroyedTower'
APPCONF = APP + '.conf'
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
CONFIG_APP_DIR = os.path.join(CONFIG_DIR, APP)
CONFIG_FILE = os.path.join(CONFIG_APP_DIR, APPCONF)
PARAMS = {'token': "622283439:AAHA71tjo0yBz5oHWHhXRI_FlpVi7ISCZW0",
          'channel_id': None}

################################# NUESTROS DATOS ###############################


###################### PARTE DEL CÓDIGO DE ARRANQUE ############################

if not os.path.exists(CONFIG_APP_DIR):
    os.makedirs(CONFIG_APP_DIR)


class Configuration(object):
    def __init__(self):
        self.params = PARAMS
        self.read()

    def get(self, key):
        try:
            return self.params[key]
        except KeyError as e:
            print(e)
            self.params[key] = PARAMS[key]
            return self.params[key]

    def set(self, key, value):
        self.params[key] = value

    def reset(self):
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        self.params = PARAMS
        self.save()

    def set_defaults(self):
        self.params = PARAMS
        self.save()

    def print_config(self):
        pprint(self.params)

    def read(self):
        try:
            f = codecs.open(CONFIG_FILE, 'r', 'utf-8')
        except IOError as e:
            print(e)
            self.save()
            f = codecs.open(CONFIG_FILE, 'r', 'utf-8')
        try:
            self.params = json.loads(f.read())
        except ValueError as e:
            print(e)
            self.save()
        f.close()

    def save(self):
        f = codecs.open(CONFIG_FILE, 'w', 'utf-8')
        f.write(json.dumps(self.params))
        f.close()

######################### PARTE CONVERSACIÓN ###################################
HELLO, BIEN, NAME = range(3)
d_users={}
ranking=rank.Ranking("Ranking")
ranking.ReadTXT()
print(ranking.printRanking())
to_type=[]

################################# DIÁLOGOS #####################################
import traceback

try:
    def text(bot,update):
        text=update.message.text
        text_out=elimina_tildes(text)
        id=update.message.chat.id
        myuser=d_users[id]
        print(text)
        print(id)
        
        if(text=="/start"):
            NAME=start(bot,update)
            return NAME
        
        if(text=="/info"):
            timer=myuser.u_timer.print_time()
            cadena=myuser.u_motxilla.PrintMotxilla()
            to_send=("Temps Restant:\n"+timer+"\n\n"+"Contingut de la motxilla:\n"+cadena)
            update.message.reply_text(text=(to_send))
        
        if(text=="/cancel"):
            update.message.reply_text(
                        text="HAS ATURAT LA CONVERSACIÓ")
            update.message.reply_text(text=("PER COMENÇAR UNA NOVA PARTIDA PREM: /start \n"),
                                      reply_markup=ReplyKeyboardRemove())
            del(myuser)
            return ConversationHandler.END
        
        global to_type
        
        print(to_type)
        
        s=text.encode('utf-8')
        print(s)
        
        if([s] in to_type):
            if(text=="Game Over"):
    
                timer=myuser.u_timer.print_time()
                update.message.reply_text(text=("HAS MORT!!\n"))
                update.message.reply_text(text=("EL TEMPS RESTANT ERA: *" + timer+"*\n"),
                                          parse_mode=telegram.ParseMode.MARKDOWN)
                update.message.reply_text(text=("PER COMENÇAR UNA NOVA PARTIDA PREM: /start \n"),
                                          reply_markup=ReplyKeyboardRemove())
                del(myuser)
                return ConversationHandler.END
            
            if(text=="End Game"):
                timer=myuser.u_timer.print_time()
                update.message.reply_text(text=("HAS ACONSEGUIT SORTIR DE LA TORRE, CONGRATULATIONS!!\n"))
                update.message.reply_text(text=("EL TEMPS RESTANT ERA: *" + timer+"*\n"),
                                          parse_mode=telegram.ParseMode.MARKDOWN)
                ranking.AddtoRanking(myuser)
                update.message.reply_text(text=(ranking.printRanking(myuser.u_nom)+"\n"),
                                          parse_mode=telegram.ParseMode.MARKDOWN)
                update.message.reply_text(text=("PER COMENÇAR UNA NOVA PARTIDA PREM: /start \n"),
                                          reply_markup=ReplyKeyboardRemove())
                update.message.reply_text(text=("----* RECOMANA EL JOC REENVIANT EL MISSATGE SEGÜENT *----"),
                                          parse_mode=telegram.ParseMode.MARKDOWN)
         
                cadena="He aconseguit sortir de la torre en: " + timer + "\n"
                cadena+="Sóc un dels pocs que ha sortit. Ets capaç d'aconseguir-ho? Prova-ho!\n"
                cadena+="Inicia una conversa amb @TestPruebauab_bot i prem /start\n"
                cadena+="No crec que pugis superar-me :)\n"
                
                update.message.reply_text(text=(cadena),
                                          reply_markup=ReplyKeyboardRemove())
                del(myuser)
                return ConversationHandler.END
        
            to_send=myuser.options[text_out].texto_enviar
            print(to_send)
            
            to_type=myuser.options[text_out].lista_opciones
            myuser.u_timer.restar_seg(myuser.options[text_out].time)
            to_send,to_type=myuser.options[text_out].realizar_modf(myuser,to_send,to_type)
            
            print("X")
            for x in to_send:
                if(x[0]=="text"): 
                    update.message.reply_text(text=(x[1]),
                                              reply_markup=ReplyKeyboardMarkup(to_type,one_time_keyboard=True))
                    time.sleep(0.5)
                if(x[0]=="image"):
                    #bot.send_photo(chat_id=id, photo=open(x[1], 'rb'))
                    time.sleep(1)
                if(x[0]=="video"):
                    bot.send_video(chat_id=id, video=open(x[1], 'rb'), supports_streaming=True)
                    time.sleep(1)
                if(x[0]=="audio"):
                    bot.send_voice(chat_id=id, voice=open(x[1], 'rb'))
                    time.sleep(1)
                if(x[0]=="location"):
                    data=x[1].split(',')
                    bot.send_location(chat_id=id, latitude=data[0], longitude=data[1])
                    time.sleep(1)
                    
            print("OK")
        else:
            print("BAD ERROR")
        
        return HELLO
    
    def start(bot,update):
        update.message.reply_text(text=("Aquest es el rànquing actual:\n\n" + ranking.printRanking()))
        update.message.reply_text(text=("Introdueixi el seu nom per començar la partida"))
        return NAME
    
    def name(bot,update):
        try:
            print(update.message.text)
            text=elimina_tildes(update.message.text)
            id=update.message.chat.id
            d_users[id]=t4.User(text,id)
            update.message.reply_text(text=("Usuari *" + text + "* creat correctament!"),
                                          parse_mode=telegram.ParseMode.MARKDOWN)
            update.message.reply_text(text=("Recorda que pots consultar el temps restant i el contingut de la motxilla amb /info i pots aturar la conversa amb /cancel"))
            update.message.reply_text(text="Prem start per començar la partida",
                                      reply_markup=ReplyKeyboardMarkup([["start"]],one_time_keyboard=True))
            global to_type
            to_type=[["start"]]
            return HELLO
        except Exception:
            traceback.print_exc()
        
    def elimina_tildes(cadena):
        s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
        return s

except Exception:
    traceback.print_exc()
