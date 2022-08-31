from requests import get, post

class TrafficAPI():
    def __init__(self) -> None:
        pass

    def send_data(self, data: dict):
        try:
            r = post('http://127.0.0.1:8000/',json=data)
            return r.content


        except Exception as e:
            return e
