#from ai_system import AI
import ai_system

"""
Main file in /AI
"""

class AI():
    def __init__(self) -> None:
        pass

    def __main__(self, message, context: list = []):
        """
        Call functions from crud file
        """
        C = ai_system.AI()

        
        if context: r = C.getMessage(message, context)
        else: r = C.getMessage(message) 

        if not r: #Message wasn't received
            #None received
            if context:
                nt = C.messageNtFound(message, context)
                if nt: return nt
                else: return 

            nt = C.messageNtFound(message)
            print(nt)
            if nt: return nt
            else: return 

        return r

    def learnNew(self, message_learn: str, response_: dict):
        #Learn new words
        C = CRUD()

        att = C.learnNew(message_to_learn=message_learn, response=response_)
        return att
        
        