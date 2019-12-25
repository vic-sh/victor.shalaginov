import telebot
import constants
import telnetlib
import OltHuaweiList

bot = telebot.TeleBot(constants.token)

bot.send_message(chat_id=constants.chatid, text='_HandlerStarted_')


def telnet_host_time(host_ip):
    try:
        tn = telnetlib.Telnet(host_ip, 23)
    except:
        return bot.send_message(constants.chatid, 'Telnet Server Unavailable')
    tn.read_until(b'login:')
    tn.write(b'admin\r')
    tn.read_until(b'Password:')
    tn.write(b'cyber\r')
    tn.read_until(b'#')
    tn.write(b'sh clock\r')
    line = str(tn.read_until(b'#'))
    line = line.split('\\r\\n')[1]
    tn.write(b'exit\r')
    tn.close()
    return bot.send_message(constants.chatid, line)


def telnet_host_ipro(host_ip):
    try:
        tn = telnetlib.Telnet(host_ip, 23)
    except:
        return bot.send_message(constants.chatid, 'Telnet Server Unavailable')
    tn.read_until(b'login:')
    tn.write(b'admin\r')
    tn.read_until(b'Password:')
    tn.write(b'cyber\r')
    tn.read_until(b'#')
    tn.write(b'sh ip ro\r')
    line = str(tn.read_until(b'#'))
    lines = line.split('\\r\\n')[9:]
    for lnln in lines:
        lnln = lnln.split()
        if len(lnln) > 6:
            bot.send_message(constants.chatid, lnln[1] + ' ' + lnln[0])
#           print(lnln[1] + ' ' + lnln[0])
    tn.write(b'exit\r')
    tn.close()
    return line


def telnet_monitor():
    try:
        tn = telnetlib.Telnet(b'10.0.0.10', 23)
    except:
        return bot.send_message(constants.chatid, '10.0.0.10 Unavailable')
    tn.read_until(b'Username:')
    tn.write(b'admin\r')
    tn.read_until(b'Password:')
    tn.write(b'admin791\r')
    tn.read_until(b'#')
    tn.write(b'conf t\r')
    tn.read_until(b'#')
    tn.write(b'sh int eth6.3 | include line\r')
    t = tn.read_until(b'#').splitlines()
    if b'administratively' in t[1]:
            tn.write(b'int eth6.3\r')
            tn.read_until(b'#')
            tn.write(b'no shutdown\r')
            tn.read_until(b'#')
            tn.write(b'quit')
            return bot.send_message(constants.chatid, 'Monitor enabled')
    elif b'not connect' in t[1]:
            tn.write(b'quit')
            return bot.send_message(constants.chatid, 'Monitor link down')
    elif b'connect' in t[1]:
            tn.write(b'int eth6.3\r')
            tn.read_until(b'#')
            tn.write(b'shutdown\r')
            tn.read_until(b'#')
            tn.write(b'quit')
            return bot.send_message(constants.chatid, 'Monitor disabled')


def telnet_wifi():
    try:
        tn = telnetlib.Telnet(b'10.22.22.99', 23)
    except:
        return bot.send_message(constants.chatid, '10.22.22.99 Unavailable')
    tn.read_until(b'login: ')
    tn.write(b'admin\r')
    tn.read_until(b'Password: ')
    tn.write(b'liver_777\r')
    tn.read_until(b'WAP->')
    tn.write(b'get wireless\r')
    t = tn.read_until(b'WAP->').splitlines()
    if b'enable' in t[1]:
            tn.write(b'set wireless disable\r')
            tn.read_until(b'WAP->')
            tn.write(b'set apply\r')
            tn.read_until(b'WAP->')
            tn.write(b'exit\r')
            return bot.send_message(constants.chatid, 'CyberNet_320 Disabled')
    elif b'disable' in t[1]:
            tn.write(b'set wireless enable\r')
            tn.read_until(b'WAP->')
            tn.write(b'set apply\r')
            tn.read_until(b'WAP->')
            tn.write(b'exit\r')
            return bot.send_message(constants.chatid, 'CyberNet_320 Enabled')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if str(message.from_user.id) == constants.chatid:
        if 'time' in message.text:
            telnet_host_time(str(message.text).split('-')[1])

        elif 'ipro' in message.text:
            telnet_host_ipro(str(message.text).split('-')[1])
#           clockstr = telnet_hosttime(str(message.text).split('-')[1])
#           bot.send_message(constants.chatid, 'NOpe')
#           elif 'ip' in message.text:
#           bot.send_message(constants.chatid, str(message.text).split('-')[1])

        elif 'olthdelall' in message.text:
            OltHuaweiList.delete_all()


#        elif 'olthsnch' in message.text:
#            delete_all.delete_all_hu()

#        elif 'olthsnchr' in message.text:
#            delete_all.delete_all_hu()

        elif 'mon' in message.text:
            telnet_monitor()

        elif 'wifi' in message.text:
            telnet_wifi()

        elif '/help' in message.text:
            bot.send_message(constants.chatid, 'time-$ip, ipro-$ip, olthdelall, mon, wifi')

        else:
            bot.send_message(constants.chatid, 'Try /help')

    else:
        bot.send_message(message.from_user.id, 'Not Allowed')


bot.polling(none_stop=True)
