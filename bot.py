import subprocess
import telebot
import config

bot = telebot.TeleBot(config.apikey)
users = {}

@bot.message_handler(commands=['start'])
def hello_user(m):
    if m.chat.id not in users.keys():
        users[m.chat.id] = {'username': m.chat.username}
    bot.send_message(m.chat.id, 'Welcome user. This bot will help you to manage a server running\
    shell comands througt it.\n If you experiment any issue or have\
    any suggestion, just let me know.\n Made with <3 @Joex23.')
    print(users)
            
@bot.message_handler(commands=['repeat_command'])
def repeat_command(m):
    print(users)
    try:
        m.text = users[m.chat.id]['last_command']
        execute_command(m)
    except:
        bot.send_message(m.chat.id, 'You haven\'t executed any command yet.')

@bot.message_handler(func=lambda m: True)
def execute_command(m):
#    print(m)
    print(users)
    if m.chat.id!=config.myid:
        return
    try:
        users[m.chat.id]['last_command'] = m.text
        command=m.text.split('/')[1]
        print(command)
    except:
        bot.send_message(m.chat.id, 'Commands should start with "/"')
        return    
    result=subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.returncode)
    print(result.stdout)
    print(result.stderr)
    if result.returncode is 0:
        bot.send_message(m.chat.id, '```\n'+result.stdout.decode('utf-8')+'```', parse_mode='Markdown')
    else:
        try:
            bot.send_message(m.chat.id, '```\n'+result.stderr.decode('utf-8')+'```', parse_mode='Markdown')
        except:
            bot.send_message(m.chat.id, '`Your command didn\'t return nothing.`', parse_mode='Markdown')

print('Running')
bot.polling()
