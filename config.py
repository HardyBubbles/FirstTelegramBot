#!/usr/bin/python

import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет! Я - EchoBot.
Я буду возвращать тебе все те добрый слова, которые ты мне напишешь. Просто скажи что-нибудь милое и я повторю тоже самое тебе!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'О, ты русский? Привет-привет!')
    else:
        bot.reply_to(message, message.text)


bot.polling(none_stop=True)