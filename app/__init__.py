try:
    from . import BOT, serverAPI
    from serverAPI import server
    from var.var import vars
    
except ModuleNotFoundError:
    from . import BOT, serverAPI
    from app.serverAPI import server
    from .var.var import vars
