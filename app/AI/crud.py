from pymongo import MongoClient
from os.path import abspath, dirname
from sys import path
dir_ = dirname(abspath('app')).split('app')[0]
path.append(dir_+'/app/var')
from var import vars

class CRUD():
    """
    Define variables scraping from database. 
    """
    DBG_ = vars()
    
    databaseJson = DBG_.database()  #Import database parameter in var/data.json
    link_connection = "mongodb://{host}:{port}".format(host=databaseJson['host'], port=int(databaseJson['port'])) #create a connection link
    db_ = str(databaseJson['talk']['database'])   #Database name      
    cl_ = str(databaseJson['talk']['collection']) #Collection name

    connection = MongoClient(link_connection) #Create a connection
    database = connection[db_] #Database
    collection = database[cl_] #Collection


    """
    values in DB.

    Check the documentation to a better compression

    """
    MSG_RCV = 'MESSAGE_RECEIVED'
    MSG_R = 'message'
    RESP = 'RESPONSE'

        


        

    

    

