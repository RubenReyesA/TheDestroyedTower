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
import bot2 as tf

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler)

######################### INFORMATION FOR APP ##################################

APP = 'destroyedtower'
APPNAME = 'TheDestroyedTower'
APPCONF = APP + '.conf'
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
CONFIG_APP_DIR = os.path.join(CONFIG_DIR, APP)
CONFIG_FILE = os.path.join(CONFIG_APP_DIR, APPCONF)
PARAMS = {'token': "622283439:AAHA71tjo0yBz5oHWHhXRI_FlpVi7ISCZW0",
          'channel_id': None}
######################### PARTE CONVERSACIÓN ###################################
HELLO, BIEN, NAME = range(3)

################################# MAIN #########################################

def main():
    # Create the EventHandler and pass it your bot's token.
    configuration = tf.Configuration()
    token = configuration.get('token')
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    

################################# CONVERSACIÓN #################################

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', tf.start)],

        states={
            HELLO: [MessageHandler(Filters.all, tf.text)],
            NAME: [MessageHandler(Filters.all, tf.name)]
        },

        fallbacks=[CommandHandler('cancel', tf.text)]
    )

################################# HANDLERS #####################################

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('help',tf.text))
    dp.add_handler(CommandHandler('info',tf.text))
    dp.add_handler(CommandHandler('cancel',tf.text))
    updater.start_polling()
    updater.idle()

################################# ARRANQUE #####################################
if __name__ == '__main__':
    main()
