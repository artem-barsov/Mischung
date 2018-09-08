import os
import telebot
import logging
from flask import Flask, request

try:
    import ujson as json
except ImportError:
    import json

token = "688343184:AAGnRwbHccoACNsrWr3N75_wnSesvp4t5dA"
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    # json_of_message = json.dumps(message)
    bot.reply_to(message, message.chat)

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
