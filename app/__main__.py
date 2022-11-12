from multiprocessing import Process
from .BOT.bot import BOT
from . import server
from os import system
from requests.exceptions import ReadTimeout
from telebot.apihelper import ApiTelegramException
from sys import exit, setrecursionlimit
import platform



def server():
    system('cd app/serverAPI && uvicorn server:APP --reload') #Run api server
    
 

    

def bot():
    try:
        BOT().bot() #Run telegram bot

    except ApiTelegramException as e:
        print(e)
        exit()

    
        
if __name__ == '__main__': #Run in paralell
  p1 = Process(target=server)
  p2 = Process(target=bot)
  
  p1.start()
  p2.start()

  p1.join()
  p2.join()
