import argparse
from os import getcwd, path
import telebot
import subprocess
from getpass import getuser
import platform

#args parser
def to_list(admins):
    return [x.strip() for x in admins.split(',')]
parser = argparse.ArgumentParser(description='Control your server or computer trought telegram.')
parser.add_argument('--api-key', required=True)
parser.add_argument('--admins', required=True, type=to_list)
args = parser.parse_args()

#create auxiliar script
if path.isfile('script_aux.sh'):
    with open('script_aux.sh', 'w') as script:
        script.write('cd $1;eval $2;error=$?;echo `pwd`;exit $error')
        script.close()

#initialization 
os = platform.system()
if os=='Windows':
    get_working_directory = 'cd'
    concat_symbol = ' & '
elif os=='Linux':
    get_working_directory = 'pwd'
    concat_symbol = ' ; '    

machine_user = getuser()
working_directory = getcwd()
users = {}
bot = telebot.TeleBot(args.api_key)


#main content
@bot.message_handler(commands=['repeat_command'])
def repeat_command(m):
    user = m.from_user.username
    try:
        m.text = users[user]['commands_list'][-1]
        execute_command(m)
    except:
        bot.send_message(m.chat.id, 'You haven\'t executed any command yet.')

        
@bot.message_handler(func=lambda m: True)
def execute_command(m):
    user = m.from_user.username
#    print(m)
    if user not in args.admins:
        bot.reply_to(m, 'No eres uno de los administradores. Cierra la puerta al salir')
        return
    if user not in users.keys():
        users[user] = {'username': user, 'wd': working_directory}
        users[user]['commands_list'] = []
        bot.reply_to(m, '[bot]> Se te ha dado de alta en la lista de usuarios')
    prompt = '['+user+'@'+machine_user+']> ' + m.text + '\n'
    wd=users[user]['wd']
    prep='./script_aux.sh "{}" "{}"'.format(wd, m.text)
#    print(prep)
    result=subprocess.run(prep, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode is 0:
        output=result.stdout.decode('utf-8')[:-1]
        bot.reply_to(m, '```\n'+prompt+(output[:output.rfind('\n')] if output.find('\n') != -1 else '')+'```', parse_mode='Markdown')
        users[user]['wd'] = output[output.rfind('\n')+1:]
        users[user]['commands_list'].append(m.text)
    else:
        try:
            output=result.stderr.decode('utf-8')
            bot.reply_to(m, '```\n'+prompt+(output[:output.rfind('\n')] if output.find('\n') != -1 else '')+'```', parse_mode='Markdown')
            if result.returncode != 127:
                users[user]['wd'] = output[output.rfind('\n')+1:]
                users[user]['commands_list'].append(m.text)
        except:
            bot.reply_to(m, '`Your command didn\'t return nothing.`', parse_mode='Markdown')        

            
print('Running')

bot.polling()
