from . import vars
from requests import post
from urllib3.connection import HTTPConnection

"""
Make requests to api server
"""

class HTTP():
    def __init__(self):
        self.addr: str = vars().server() #Get the address of api server and port, ex.: 127.0.0.1:800
        

    def sendMessage(self, message, context: list = []):
        try:
            if context:
                r = post(self.addr+'/sendMessage', params={'message':message})
                return r.content.decode('utf-8').replace('"', '')

            r = post(self.addr+'/sendMessage', params={'message': message})
            return r.content.decode('utf-8').replace('"', '')

        except HTTPConnection:
            pass
    
    def learnNew(self, message_learn: str, data_response: dict):
        r = post(self.addr+'/learnNew', params={'message': message_learn}, json=data_response)
        return r.content.decode()