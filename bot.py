import os
import telebot
import logging
import json
from flask import Flask, request
from datetime import datetime
from telebot import types

token = "688343184:AAGnRwbHccoACNsrWr3N75_wnSesvp4t5dA"
bot = telebot.TeleBot(token)

from json import JSONEncoder
class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
showJSON = 'show json : off'
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'audio', 'video', 'document', 'location', 'contact', 'sticker', 'game', 'video_note', 'voice', 'venue', 'new_chat_member', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message', 'invoice', 'successful_payment', 'connected_website'])
def echo_message(message):
    global showJSON
    markup = types.ReplyKeyboardMarkup()
    markup.row(showJSON)
#    bot.send_message(message.chat.id, reply_markup=markup)
    if message.text == showJSON:
        if message.text == 'show json : off':
            showJSON = 'show json : on'
        else:
            showJSON = 'show json : off'
    elif showJSON == 'show json : on':
        bot.reply_to(message, MyEncoder().encode(message))
    bot.reply_to(message, datetime.utcfromtimestamp(message.forward_date+18000).strftime('%H:%M:%S %d-%m-%Y'))

if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)
    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://tgb-ot.herokuapp.com/bot")
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    bot.remove_webhook()
    bot.polling(none_stop=True)
