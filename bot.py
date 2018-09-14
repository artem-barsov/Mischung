import os
import telebot
import logging
from flask import Flask, request
import json
import psycopg2
import sys

token = "688343184:AAGnRwbHccoACNsrWr3N75_wnSesvp4t5dA"
bot = telebot.TeleBot(token)
con = None

from json import JSONEncoder
class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    json_of_message = MyEncoder().encode(message)
    try:
        con = psycopg2.connect("dbname='Updates'")
        cur = con.cursor()
        cur.execute("INSERT INTO Updates(messages) VALUES (%s)", json_of_message)
        con.commit()

    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
        print('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()
    bot.reply_to(message, json_of_message)

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
        return "<h1>?</h1><h2>?</h><h3>?</h><h4>?</h><h5>?</h><h6>?</h>", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    bot.remove_webhook()
    bot.polling(none_stop=True)
