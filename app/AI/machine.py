from crud import CRUD 

class AI():
    def __init__(self) -> None:
        pass

    def __main__(self, message, context: list = []):
        if context:
            return CRUD().getMessage(message, context)
            
        return CRUD().getMessage(message)