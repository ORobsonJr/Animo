 

class vars():
    from json import loads
    try:
        from os import getcwd
        
        with open('app/var/data.json', 'r') as f: #read data.json
            raw_data = loads(f.read())

    except Exception as e:
        raw_data = e

    def database(self):
        return vars.raw_data['database'] #Return database parameters
    
    def server(self, routeAPI: str = ''):
        route = vars.raw_data['server'] #Return server api parameters

        if not routeAPI:
            return route['host']

        
        return route[routeAPI]

    def bot_token(self):
        data = input("Digite seu token: ")
        return data