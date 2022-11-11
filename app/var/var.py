from sys import exit

class vars():
    def __init__(self) -> None:
        from json import loads
        try:        
            with open('/home/linuxlite/animo/app/var/data.json', 'r') as f: #read data.json
                self.raw_data = loads(f.read())

        except Exception as e:
            print("[ERROR] A error happend in a important part of program, unfortunately we need close everything :(\n",e)
            exit()


    def database(self):
        return self.raw_data['database'] #Return database parameters
    
    def server(self, routeAPI: str = ''):
        route = self.raw_data['server'] #Return server api parameters

        if not routeAPI:
            return route['host']

        
        return route[routeAPI]

    def bot_token(self):
        with open('app/var/bot_token', 'r') as f:
            content: str =  f.read() #Get the content
            return content.replace('\n', '') #Replace the special character

