from pymongo import MongoClient
from random import choice
import sys
sys.path.append('../')
from var.var import vars
from string import ascii_letters



class DB(): #Handle server requests
    def __init__(self):
        self.databaseJson = vars().database() #Import database parameter in var/data.sjon
        self.link_connection = "mongodb://{host}:{port}".format(host=self.databaseJson['host'], port=int(self.databaseJson['port'])) #create a connection link
        db_ = str(self.databaseJson['server']['database'])        
        cl_ = str(self.databaseJson['server']['collection'])


        self.connection = MongoClient(self.link_connection)
        self.database = self.connection[db_]
        self.collection = self.database[cl_]
        

    def checkUniqueID(self, uniqueID: str):
        #Check if uniqueID is really unique
        for x in self.collection.find({}, {"unique_id": uniqueID}):
            return 200 #this unique id already exists
        return 404 #id not found 

    def storeData(self, data):
        lista = [ascii_letters]
        ID = []

        try:
            
            if DB().checkUniqueID(uniqueID=' '.join) ==404:
                self.collection.insert_one(data) #Insert data into collection
            return 200
        except Exception as e:
            return e

    def removeDocument(self, request: int, UniqueID: str): #Delete a request
        if request ==200:
            try:
                self.collection.delete_one({'unique_id':UniqueID})
                return 200
            except:
                return 503
        else:
            return 400

    def returnRequest(self, UniqueId: str):
        d = self.collection.find({}, {'unique_id': UniqueId})
        for data in d:
            return data
        return 404


   
        




        

    

