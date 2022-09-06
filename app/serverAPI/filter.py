from pymongo import MongoClient
from random import choice #Variables 
from sys import path
path.append('../')

from var import *
from difflib import SequenceMatcher


"""
Make requests in database
"""

class filter():
    def __init__(self):
        self.databaseJson = vars().database() #Import database parameter in var/data.sjon
        self.link_connection = "mongodb://{host}:{port}".format(host=self.databaseJson['host'], port=int(self.databaseJson['port'])) #create a connection link
        db_ = str(self.databaseJson['talk']['database'])   #Database name      
        cl_ = str(self.databaseJson['talk']['collection']) #Collection name

        self.connection = MongoClient(self.link_connection)
        self.database = self.connection[db_]
        self.collection = self.database[cl_]
        self.blacklist = self.database['blacklist']

    def randomMessage(self, message: str, learn: bool = None, response: str = ''):
        message = message.upper()

        data = self.collection.find_one({"message": message})

        if data != None: #If found document return
            return choice(data['response']) #Return a random message

        #Return a similar word
        if data ==None:
            get_messages = [x for x in self.collection.find({}, ['message'])] #Scrape all words
            messages = []
            for m in get_messages:
                messages.append(m['message'])
            
            similar_values = []
            for similar in messages:
                similar_values.append(SequenceMatcher(None, message, similar).ratio()) #Add the level of similarity between words

            localiza = messages[similar_values.index(max(similar_values))] #Return me message more similar 
            object = self.collection.find_one({'message': localiza}) #Find a document using filter above
            return choice(object['response']) #Return a random similar response

        #Learn a new word
        else:
            if learn == True: #Learn a new word passing by a process
                filter = self.blacklist.find_one({'message': message})
                if filter != None: #A bad word was identify
                    return "Eita kk"

                self.collection.insert_one({
                    "message": message,
                    "response": [response]
                })

                return 

                

            return "Desculpe, mas não consegui entender o que quis dizer"
            


        
        

