from multiprocessing import Process
from .BOT.bot import BOT
from . import server
from os import system

def server():
    print(system('pwd'))
    try: system('cd app/serverAPI/ && uvicorn server:APP --reload') #Run api server
    except Exception as e: print('[ERRO_SERVER]',e)

def bot():
    BOT().bot() #Run telegram bot

if __name__ == '__main__': #Run in paralell
  p1 = Process(target=server)
  p2 = Process(target=bot)
  
  p1.start()
  p2.start()

  p1.join()
  p2.join()
