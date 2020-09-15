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

import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler)

import testbot2 as tb2
import test3 as t3
import test4 as t4
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
dict={}
mochila=["Linterna", "Llave"]

def print_mochila(mochila2):
    cadena=""
    for x in mochila2:
        cadena += x +" --> 1\n"
    return (cadena)

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
hola=0
################################# DIÁLOGOS #####################################

def start(bot,update):
    id=update.message.chat.id
    bot.send_chat_action(chat_id=id, action=telegram.ChatAction.TYPING)
    time.sleep(1)
    bot.send_message(chat_id=id, text="Dimecres 13 de Maig del 2069.")
    bot.send_message(chat_id=id, text="Tretze dies després de l'apagada mundial tecnològica provocada per part de la unió de hackers ANONYMOUS, segons la premsa, tot el planeta ha estat treballant per recuperar la normalitat. Dies després de l'apagada, vas estar indegant en trobar-ne els culpables. Formes part d'un grup secret de hackers de barret blanc que està investigant el cas. Mentres t'apropaves als culpables, et van trobar i et van sedar. T'han segrestat i t'han deixat en una de les seves torres secretes de control. Pensaven que estaves mort després de la pallissa que et va donar el cap. Però no, segueixes viu. Tots han fugit de la torre, però han programat la seva autodestrucció per eliminar qualsevol rastre de la seva activitat en el seu servidor central. Tens 20 minuts per sortir-ne i desemmascarar als culpables.")
    bot.send_chat_action(chat_id=id, action=telegram.ChatAction.UPLOAD_PHOTO)
    time.sleep(1)
    bot.send_location(chat_id=id, latitude=41.500237, longitude=2.111677)
    update.message.reply_text(text=("Benvingut a 'THE DESTROYED TOWER'. Com et dius?"),
                              reply_markup=t3.generar_teclat(t3.teclats["hab1porta"]))
    return HELLO

def hello(bot,update):
    if(update.message.text=="PUERTA"):
        puerta(bot,update)
    if(update.message.text=="VENTANA"):
        BIEN = ventana(bot,update)
        return BIEN

def puerta(text, bot,update):
    id=update.message.chat.id
    bot.send_chat_action(chat_id=id, action=telegram.ChatAction.UPLOAD_AUDIO)
    time.sleep(1)
    bot.send_voice(chat_id=id, voice=open('soundDoor.ogg', 'rb'))
    bot.send_chat_action(chat_id=id, action=telegram.ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text(text=("Gracias por usar Telegram, bienvenidos a la Destroyed Tower, Encantado " + text +"!"),
                    reply_markup=t3.generar_teclat(t3.teclats["hab1portasortir"]))
    tb2.clock.restar_seg(10)
    return HELLO

def bien(bot,update):
    print(update.message.text)
    if(update.message.text=="VOLVER"):
        HELLO = puerta(bot,update)
        return HELLO
    if(update.message.text=="FIN"):
        return ConversationHandler.END


def ventana(bot,update):
    print(update.message.text)
    bot.send_audio(chat_id=update.message.chat.id, audio=open('Yiruma.m4a', 'rb'))
    reply_keyboard2 = [['VOLVER'],["FIN"]]
    update.message.reply_text(text="Gracias por usar Telegram JAJAJAJAJ!",
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True))
    return BIEN


def name(bot,update):
    print(update.message.text)
    update.message.reply_text(
                    text="Encantado Don José!!",
                    reply_markup=ReplyKeyboardRemove())
    return NAME

def cancel(bot,update):
    update.message.reply_text(
                    text="HAS CANCELADO LA CONVERSACIÓN")
    dict.pop(update.message.chat.id)
    return ConversationHandler.END

def help(bot,update):
    update.message.reply_text(
                    text="Bienvenido a ¡The Destroyed Tower!\nSoy __ y estoy aquí para ayudarte.\nPara empezar a jugar, haz click aquí: /start")

def info(bot,update):
    update.message.reply_text(
                    text=("Tiempo Restante: "+ tb2.clock.print_time())
    )
    
#copy.deep.copy(X)
#del(X)
    
def text(bot,update):
    text=update.message.text
    global hola
    print(text)
    print(hola)
    if(text=="/start"):
        hola=1
        return start(bot,update)
    if(text=="PUERTA"):
        return puerta(text,bot,update)
    if(hola==1):
        hola=0
        return puerta(text,bot,update)
    update.message.reply_text(
                    text="ESE MENSAJE NO EXISTE")
    
