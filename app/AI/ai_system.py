from pymongo import MongoClient
from os.path import abspath, dirname
from sys import path
dir_ = dirname(abspath('app')).split('app')[0]
path.append(dir_+'/app/var')
from var import vars
from difflib import get_close_matches as matches
from random import choice
from crud import CRUD



"""
Create the system of Artificial Inteligence, to a better compression,  check the documentation...

"""

CR = CRUD


def similarity(list1: list, list2: list):
    """
    Analyze the level of similarity between two lists

    The same word = 2 points
    Similar word = 1 point
    """
    #Lists to uppercase, to avoid conflicts between lowercase and uppercase
    l1 = [i.upper() for i in list1]
    l2 = [l.upper() for l in list2] 


    duplicates: int = len(l1+l2) - len(set(l1+l2)) * 2 #The number of words repeated
    
    count_list = [] #The number os similar words founded
    for i in l1: count_list.append(matches(i, l2)) #Append similar words

    """
    If it returns 0, it's because the list doesn't have items good enough to be evaluated."""
    return len(count_list) + duplicates #Return the level of similarity between both lists
    

def get_vowels_db(msg_sended: str, message_reference: str):
    """
    Display whether the word is the same word, however with variations of vowels
    """
    vowels = ['A','E','I','O','U'] #Need be in uppercase

    msg1 = [x for x in msg_sended.upper() if x not in vowels] #Delete the vowals and leaves only consonants
    msg2 = [x for x in message_reference.upper() if x not in vowels]

    logic1, logic2 = ''.join(msg1), ''.join(msg2) #Groups elements in a string

    if logic1 == logic2:
        #Are the same word, but probably with additionals vowels
        return True

    #Different words
    return False


def update_querys(message, response_location, frequency_location):
    """
    Update documents in Database
    """

    get_it = CR.collection.find_one({CR.MSG_RCV: message}) #Get the documment in DB

    #Update the frequency in RESPONSE array
    CR.collection.update_one({
    "MESSAGE_RECEIVED": message,'RESPONSE.message': frequency_location[CR.MSG_R]  
    }, {'$set':{'RESPONSE.$.frequency':  frequency_location['frequency']+1}})


    #Update FREQUENCY
    att = CR.collection.update_one({CR.MSG_RCV: message}, {'$set': {'FREQUENCY': frequency_location['frequency']+1}})




    
class AI():
    """
    The system of AI, usually receive message, process and return response
    """
    def __init__(self):
        pass
    

    def getMessage(self, message: str, context: list = []):
        """
        Get a message whose match to message received.

        Obs.: The message need be the same, otherwise it return None.
        """
        message = message.upper() #We need update message to uppercase 'cause for default messages are saved in the same way

        #try:
        
        simi_ = []

        try:
            get_it = CR.collection.find_one({CR.MSG_RCV: message}) #Get the documment in DB
            response = get_it['RESPONSE'] #Get the argument "response" from get_it dict, please read the documentation to understand what i'm saying...

            if get_it: #If exist the same argument in DB, continue... 
                if context: #If keyword context was provided...
                    for res in response:
                        #Try find the most similar response, analyzing the context provided
                        sm = similarity(list1=res['context'], list2=context) #Similarity between two lists 
                        simi_.append(sm)
                    i = simi_.index(max(simi_))  #Find index where is the most similar word, considering the level in INT of list
                

                    #Update the querys
                    update_querys(message, get_it, response[i]) 

                    return response[i][CR.MSG_R]


                else: #If no context, return random
                    return_msg = choice(response)

                    #Update querys
                    update_querys(message, get_it, response[response.index(return_msg)])

                    return return_msg[CR.MSG_R]

            return 

        except TypeError:
            return 

       
            

    def learnNew(self, message_to_learn: str, response: dict):
        """
        Learn a new word or phrase whose doesn't exists on DB
        """

        #check if the message exists in database

        check = CR.collection.find_one({CR.MSG_RCV: message_to_learn})
        if not check:
            CR.collection.insert_one(
                {
            "MESSAGE_RECEIVED": message_to_learn.upper(),
            "FREQUENCY": 1,
            "RESPONSE": [response]

                })
            return None

        return 'The message sended already exists in DB, try another'



    def messageNtFound(self, message: str, context = []):
        """
        If context:
            Return a message with more context possible
        else:
            returns nothing which will be processed later
        """

        message = message.upper() #By default the message in database is stored in uppercase

        
        all_messages = CR.collection.find({}) 

        value = []

        #try:
        for raw in all_messages:
            logic = get_vowels_db(raw[CR.MSG_RCV], message)

            if logic == True:
                if context:
                    #Return the message with the most similar context
                    sm = similarity(list1=res['context'], list2=context) #Similarity between two lists in percentege
                    value.append(sm)
                    i = simi_.index(max(simi_))

                    update_querys(message=message, response_location=raw, frequency_location=raw[i]) #Update values in DB

                    return value[i][CR.MSG_R]

                choose = choice(raw[CR.RESP])
                update_querys(message=message, response_location=raw, frequency_location=choose)
                return choose[CR.MSG_R]

        return 


        

       
        

        
