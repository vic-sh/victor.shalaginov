# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)


# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, """\
Hi there, I am CallBot. Type "/call" to call\
""")
    pass


# Обработчик команд '/call' .
@bot.message_handler(commands=['call'])
def handle_call(message):
    sent = bot.send_message(message.chat.id, 'Please specify number')

    print (sent)
#    bot.register_next_step_handler(sent, hello)

# echo-bot
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

# echo-bot_photo
@bot.message_handler(content_types=["photo"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.photo)
    if message.chat.type == 'group':
     # group chat message
     photo = open('C:\\1.png', 'rb')
     bot.send_photo(message.chat.id, photo)
     bot.send_photo(message.chat.id, "FILEID")

if __name__ == '__main__':
    bot.polling(none_stop=True)
