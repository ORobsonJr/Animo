from fastapi import FastAPI
from pydantic import BaseModel
import  sys
sys.path.insert(0, '../')
from DB_server.check_requests import DB
from filter import filter

class model_data(BaseModel):
    package = {"message": ""}


APP = FastAPI()

class server():
    def __init__(self) -> None:
        pass
    
    @APP.post('/sendMessage')
    def sendMessage(message: str):
        """
        3 Filters
        First filter
        Return a random message based on message sent

        Second filter
        Try find a similar message to send

        Thrird filter
        Learn the message and use a blacklist to avoid bad 
        words
        """
        return filter().randomMessage(message)


        


if __name__ == '__main__':
    C = server()



        



        


        
    
    
