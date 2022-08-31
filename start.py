from multiprocessing import Process
#from app.bar.server import CONNECTION
from app.BOT.bot import BOT
import asyncio
from os import system
from 

def server():
    asyncio.run(system('cd app/bar/ && uvicorn server:APP --reload'))


def bot():
    BOT().bot()

if __name__ == '__main__':
  p1 = Process(target=server)
  p2 = Process(target=bot)
  
  p1.start()
  p2.start()

  p1.join()
  p2.join()
