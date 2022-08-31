import telebot, sys
sys.path.insert(0, '../')
from requests import post
from requests.exceptions import ConnectionError

class BOT():

    def bot(self):
        bot = telebot.TeleBot('5590917419:AAERbFP2hpgp8OKLjazPHovkDMg97a60G08') #Connect using API_KEY

        @bot.message_handler(content_types=['text'])
        def start(call):
            print('[BOT]MESSAGE RECEIVED: ',call.text) #Message received by bot
            
            try:
                r = post('http://127.0.0.1:8000/sendMessage?message={message}'.format(message=call.text))
                message = r.content.decode('utf-8').replace('"', '')
                print('[BOT]MESSAGE SEND: ',message)
                bot.send_message(call.chat.id, message)

            except ConnectionError:
                print('[ERROR] Connection problems')

            except Exception as e:
                print(f'[ERROR]{e}')





            

           
        bot.polling(none_stop=False)

