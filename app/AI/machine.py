from crud import CRUD 

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
        C = CRUD()

        
        if context:
            #If context keyword was provided
            r = C.getMessage(message, context) #Return message

            if not r: #Any result provided
                nt = C.messageNtFound(message, context) #Message wasn't received
                return nt

            return r

        #With no keyword context
        r = C.getMessage(message) 

        if not r: #Message wasn't received
            return C.messageNtFound(message)

        return r

    def learnNew(self, message_learn: str, response_: dict):
        #Learn new words
        C = CRUD()

        att = C.learnNew(message_to_learn=message_learn, response=response_)
        return att
        
        