from requests import post
from requests.exceptions import ConnectionError
from . import vars, crud


cy="\033[1;36m" #cyan color

req = crud.HTTP()



class BOT():
    """
    These class handle messages received, controll callback query commands sended by user in chat.

    The main role of these class is:
    * Receive message
    * Send these data and requests to api server
    * Api server process data e send another data
    * Sometimes we make little adjustes or we return it to user in a raw format.

    """
    def __init__(self):
        self.token: str = vars().bot_token() #Call api token
        self.addr: str = vars().server() #Get the address of api server and port, ex.: 127.0.0.1:800
        self.context = [] #This list store the identity of user + context
        #Context = Previously received messages, in our case is just stored 3 messages to avoid suuper contexts and overload our machine power
        #The self.context format is something like [{'user_id': 123456: 'context': ['oii', 'tudo bem?']}...]

        #Messages to response
        self.learn_message = 'Digite o que o bot deve responder quando receber essa menssagem\nObs.: Seja educado por favor'
        

    def bot(self):
        """
        Root function
        """
        from telebot import TeleBot
        from telebot import types


        bot = TeleBot(self.token) #Connect using Token
        print(cy+'[BOT]     BOT is working')

        @bot.message_handler(commands=['start']) 
        def start(call):
            """
            When the user send /start as command or in their first use
            """
            bot.send_message(call.chat.id, 'Olá')


        @bot.message_handler(content_types=['text'])
        def chatting(call):
            """
            Main function where the majority of activies happen here
            """

            """
            The context has as strucure something like:
            context = [{'user_id': 12345678:, 'context': ['oi']}, {'user_id': 87654321, 'context': ['oi, 'blz?']}]

            Basically we use context in some parts of program, and each user has your own dict whose has 2 keys:
            * user_id = A kinda of primar key, each user_id is unique per user
            * context = The last messages sended per user, it's used as context like the name suggest, but we just allow 3 elements
            to avoid machine overprocessing, then when the list is equal to 3 we remove the older element.
            """

            find_ = next((i for i, item in enumerate(self.context) if item["user_id"] == call.chat.id), None)
            #Try find the dict of user in list, return the index if exists or return None if not


            if find_ != None: #If exists...
                user_location = self.context[find_]['context']

                if len(user_location) <=2: #If dict in list had more than 3 elements, we put 2 instead because
                    #the system count the index 0 too
                    user_location.append(call.text)

                else:
                    #Remove the first element, because the list can't be bigger than 
                    #After remove, we add another message
                    if user_location:
                        print(call.text)
                        user_location.pop(0)
                        user_location.append(call.text)


            else:
                #If this user never send a message before...
                self.context.append({'user_id':call.chat.id, 'context':[call.text]}) #Add context to list

            @bot.callback_query_handler(func=lambda call_: True)
            def notfound(call_):
                """
                How logic works here...:

                *When the button is pressed, the function takes the message sent before the reply
                """
                if call_.data == 'teach':
                    find_ = next((i for i, item in enumerate(self.context) if item["user_id"] == call.chat.id), None)
                    #We need another find_ variable because the variable above had delay in this moment or code
                    reply = types.ForceReply() #Return message in a reply format
                    bot.send_message(call_.from_user.id, text='Digite o que o bot deve responder quando receber essa menssagem\n*Obs.: Seja educado por favor*', parse_mode='Markdown', reply_markup=reply)

                

            if call.reply_to_message:
                #It's in a reply model             
                if call.reply_to_message.text == self.learn_message:
                    print(call)
                    bot.edit_message_reply_markup(call.chat.id, message_id=call.id)
                    #If text in these set is the same declareted in self.learn_message...
                    find_ = next((i for i, item in enumerate(self.context) if item["user_id"] == call.chat.id), None)
                    #Find the entity of user in self.context
                    message_to_response = call.text #Message to learn
                    context_to_use = self.context[find_]['context']
                    message_to_learn = context_to_use[len(context_to_use)-2] #The response to message to learn

                    if message_to_response != message_to_learn:
                        #Message to response need be different of message to lean, if both are the same, we can't go on

                        l = req.learnNew(message_learn=message_to_learn, data_response={'message': message_to_response, 'frequency': 0, 'context': context_to_use})

                        if l:
                            print(cy+f'[BOT] MESSAGE LEARNED: "{call.text}" CONTEXT {context_to_use} RESPONSE: "{message_to_response}"')
                        else: print('[BOT] An error occured in attempt to learn message')

                 

        


            print(cy+'[BOT]     MESSAGE RECEIVED: ',call.text) #Message received by bot
            

            try:
                if len(self.context) >=3:
                    #If context has more than 3 items, send requests using context for better precision
                    message = req.sendMessage(message=call.text, context=self.context[len(context)-3:len(context)])
                else:
                    message = req.sendMessage(message=call.text)

                print('[BOT]     MESSAGE SEND: ',message) #Get the message sent by api address
                


                if message=='null' or None: #Nothing received
                    teach = types.InlineKeyboardButton('Ensinar resposta', callback_data='teach') #Create a button to teach a message to user
                    keyboard = types.InlineKeyboardMarkup()
                    keyboard.add(teach) #Add button

                    bot.send_message(call.chat.id, 'Desculpa, mas não cosegui entender o que você quis dizer :/', reply_markup=keyboard) 
                    
                else:
                    bot.send_message(call.chat.id, message)


            except ConnectionError:
                print('[ERROR]     Connection problems')

            except Exception as e:
                print(f'[ERROR]{e}')

                
        bot.polling(none_stop=False) #Create a loop
