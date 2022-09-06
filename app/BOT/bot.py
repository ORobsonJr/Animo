from requests import post
from requests.exceptions import ConnectionError
from . import vars



class BOT():
    def __init__(self):
        #vars().server()
        self.token = vars().bot_token()

    def bot(self):
        from telebot import TeleBot

        bot = TeleBot(self.token) #Connect using API_KEY
        print('[BOT] BOT is working')
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

