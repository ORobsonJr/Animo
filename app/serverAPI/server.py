from os.path import abspath, dirname
from urllib import response
from fastapi import FastAPI, Query
from pydantic import BaseModel
from sys import path
dir_ = dirname(abspath('app')).split('app')[0]
path.append(dir_+'/app/AI')
from machine import AI
from json import load
from fastapi import HTTPException
import uvicorn


APP = FastAPI() #Create api object



@APP.post('/sendMessage') #Receive message and return a resonse based in a filter and parameteres
def sendMessage(message: str, context: list = Query(default=None)): #to se more check the package filter
    a = AI()

    if context:
        a.__main__(message, context)
        
    return a.__main__(message)

@APP.post('/learnNew')
def learnNew(message: str, response: dict):
    a = AI()
    

    att = a.learnNew(message_learn = message,
    response_ = response)

    if att:
        raise HTTPException(409, att)
            


        
#if __name__ == '__main__':
    #uvicorn.run(APP, host="127.0.0.1", port=8000) #Run server
    



        



        


        
    
    
