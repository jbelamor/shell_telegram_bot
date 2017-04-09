import tempfile
import subprocess
import os
import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.apikey)

teclado = types.ReplyKeyboardMarkup(one_time_keyboard=True)
teclado.add('Potorro','Potorrin')
teclado.add('cerrar')

@bot.message_handler(commands=['hello'])
def hola(message):
    bot.send_message(message.chat.id, 'hello', reply_markup=teclado)

@bot.message_handler(func=lambda m: m.text=='Potorro')
def miau(m):
    bot.send_message(m.chat.id, 'Has seleccionado Potorro')

@bot.message_handler(func=lambda m: True)
def miau(m):
    if m.chat.id!=config.myid:
        return
    command=m.text.split('/')[1]
    print(command)
    result=subprocess.run(command + '> tmp', shell=True, stdout=subprocess.PIPE)
    bot.send_message(m.chat.id, '```'+result.stdout.decode('utf-8')+'```', parse_mode='Markdown')
    return
    for line in open('tmp'):
        if len(line)>1:
            bot.send_message(m.chat.id, '```'+line+'```', parse_mode='Markdown')
        else:
            continue
print('Running')
bot.polling()
