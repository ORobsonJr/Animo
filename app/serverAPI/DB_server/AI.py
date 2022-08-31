import jellyfish
from pymongo import MongoClient
import sys
sys.path.append('/home/linuxlite/animo/app/')
from var.var import vars
from random import choice


"""
Responsable for handle the AI system, sendind similar messages, learning new messages, identifying bad words
"""

class AI(): #Handle bot message requests
    def __init__(self):
        self.databaseJson = vars().database() #Import database parameter in var/data.sjon
        self.link_connection = "mongodb://{host}:{port}".format(host=self.databaseJson['host'], port=int(self.databaseJson['port'])) #create a connection link
        db_ = str(self.databaseJson['talk']['database'])   #Define database
        cl_ = str(self.databaseJson['talk']['collection']) #Define database collection
        bl = str(self.databaseJson['talk']['blacklist']) #Define blacklist


        self.connection = MongoClient(self.link_connection)
        self.database = self.connection[db_]
        self.collection = self.database[cl_]
        self.blackL = self.database[bl]
    

    def getSimilar(self, message): #Return the more similar message according with message sent
        getALL = self.collection.find({},{"message"}) #Get all messages
        message = message.upper() 
        
        messagens = []
        value = []

        #Get words by the first letter

        for get_ in getALL:
            msg = get_['message']
            messagens.append(msg) #Add message in list 1
            value.append(jellyfish.levenshtein_distance(message, msg)) #Add number in list 2, jellyfish function rate the similatiry between both words

        #find the minimum number
        get_min = value.index(min(value))
        getALL.close()
        return messagens[get_min]  #Return the message

    def getMessage(self, message): #Return a response from message sended 
        for metadata in self.collection.find({},{}): 
            if message.upper() ==metadata['message']:
                self.collection.close()
                return choice(metadata['response'])
            
    def unkownMessage(self, message_to_learn: str, response): #Add a response if message not found
        data = {
        "message": message_to_learn,
        "response": response
        }
        try:
            self.collection.insert_one(data)
            self.collection.close()

        except Exception as e:
            return e

    def messageLearn(self, message_send, response): #Add the most comom responses for a message
        #Search Id message in database
        message_send.upper(), response.upper()
    
        data = self.collection.find({})
        for d in data:
            if d['message']==message_send:
                try:
                    d['response'].append(response)
                    print(response)
                    self.collection.update_one({"_id": d['_id']}, {"$set": {"response":d['response']}})
                    return 
                except Exception as e:
                    return e
        return 'NotFound'

    def blackList(self, message: str):
        black_list = self.blackL.find({'message': message.capitalize()})
        
        for bl_ in black_list:
            if None:
                return
            return 'Seja mais educado! por favor.'
        
    




