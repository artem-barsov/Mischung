#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
from telepot.loop import MessageLoop
TOKEN = '680764124:AAGwTa4a6e0zx_tJcYdrr5njiCIkTVKFeiY'
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
        bot.sendMessage(chat_id, "answer: {}".format(answer))
    except:
        if text == '/start':
            bot.sendMessage(chat_id, "Hello, {}!".format(msg["from"].get("first_name").encode('utf-8')))
        elif text == '/help':
            bot.sendMessage(chat_id, u'Бот в процессе разработки.'.encode('utf-8'))
        else:
            bot.sendMessage(chat_id, text)

def UpdatesInfo():
    import telepot
    from pprint import pprint
    bot = telepot.Bot('680764124:AAGwTa4a6e0zx_tJcYdrr5njiCIkTVKFeiY')
    response = bot.getUpdates()
    pprint(response)

UpdatesInfo()
MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while True:
    if False: break
#     n = input('To stop enter "stop":')
#     if n.strip() == 'stop':
#         break
