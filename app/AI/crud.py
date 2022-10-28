from pymongo import MongoClient
from os.path import abspath, dirname
from sys import path
dir_ = dirname(abspath('app')).split('app')[0]
path.append(dir_+'/app/var')
from var import vars
from json import loads
from difflib import SequenceMatcher

"""
Make requests in database

"""

def similarity(list1: list, list2: list):
    """
    Análisa quantas palavras iguais tem
    Análisa palavras similares
    """
    from difflib import get_close_matches as matches

    l1 = [i.upper() for i in list1] #List1 to uppercase
    l2 = [l.upper() for l in list2] #List2 to uppercase
    
    
    count_list = [] #The number os similar words founded
        #The lists is completely different, nothing equal
    for i in l1:
        count_list.append(matches(i, l2)) #Append similar words


    return float(len(count_list)) #Return how many words have
    
    
class CRUD():
    def __init__(self):
        DBG_ = vars()
        
        self.databaseJson = DBG_.database()  #Import database parameter in var/data.json
        self.link_connection = "mongodb://{host}:{port}".format(host=self.databaseJson['host'], port=int(self.databaseJson['port'])) #create a connection link
        db_ = str(self.databaseJson['talk']['database'])   #Database name      
        cl_ = str(self.databaseJson['talk']['collection']) #Collection name

        self.connection = MongoClient(self.link_connection)
        self.database = self.connection[db_]
        self.collection = self.database[cl_]
        self.blacklist = self.database['blacklist']

    def getMessage(self, message: str, context: list = []):
        """
        Get a message whose match to message received
        """
        message = message.upper()

        try:
            att = self.collection.find_one({'MESSAGE_RECEIVED': message})
            response = att['RESPONSE']
            #estrutura = [{message_received: 'oi', similarity: 8}] 
            simi_ = []
            
            if att:
                if context:
                    for res in response:
                        sm = similarity(list1=res['context'], list2=context) #Similarity between two lists in percentege
                        simi_.append(sm)
                i = simi_.index(max(simi_)) 
                

                return response[i]['message']

            
        except TypeError:
            #Doesn't exists any message equivalent to message received
            return None
            

    def learnNew(self, message_to_learn: str, context: list, response: str):
        """
        Learn a new word or phrase whose doesn't exists on DB
        """

        self.collection.insert_one(
            {
        "MESSAGE_RECEIVED": message_to_learn,
        "FREQUENCY": 1,
        "RESPONSE": [
            {"message": response,
            "frequency": 0,
            "context": context #Analisa qnts palavras se encaixam com o contexto atual 
            }
            ]
            })

    

    

