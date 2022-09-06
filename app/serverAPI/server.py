from fastapi import FastAPI
import filter

APP = FastAPI() #Create api object

class server():
    def __init__(self):
        pass
    
    @APP.post('/sendMessage') #Receive message and return a resonse based in a filter and parameteres
    def sendMessage(message: str): #to se more check the package filter
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



        



        


        
    
    
