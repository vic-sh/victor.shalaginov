import telebot
import constants
import DTMF_send
import re

bot = telebot.TeleBot(constants.token)

# bot.send_message(-1001122709467, "test12345")

upd = bot.get_updates()
# print(upd)
#last_upd= ''
#if len(upd) > 1:
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Please type a number to dial (6-11 digits) or command: /help, /alarm, /prohib, /hotline')

@bot.message_handler(commands=['alarm'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Alarm test started')
    print(message.text)
    DTMF_send.launch_test_alarm()
    print('ALARM')
    bot.send_message(message.from_user.id, 'Alarm test finished, released')
    print(message.text)

@bot.message_handler(commands=['prohib'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Call prohibition test started')
    DTMF_send.launch_test_prohib()
    bot.send_message(message.from_user.id, 'Call prohibition test finished, released')

@bot.message_handler(commands=['hotline'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Hotline test started, SUBSCRIBE MUST BE ENABLED!')
    DTMF_send.launch_test_hotline()
    bot.send_message(message.from_user.id, 'Hotline test finished, released')

@bot.message_handler(content_types=('text'))
def handle_text(message):
    print(message.text)

    match = re.match('\d{6,11}$', message.text)
    if match:
       #print(match)
       print('match ok')
       DTMF_send.launch_test(message.text)
       bot.send_message(message.from_user.id, 'released')
       print(message.text)
    else:
       print('match nok')
       bot.send_message(message.from_user.id, 'Please enter a correct number to dial (6-11 digits) or type /help')

bot.polling(none_stop=True, interval=0)
