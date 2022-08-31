from json import loads

class vars():
    try:
        with open('/home/linuxlite/animo/app/var/data.json', 'r') as f:
            raw_data = loads(f.read())

    except Exception as e:
        raw_data = e

    def database(self):
        return vars.raw_data['database']