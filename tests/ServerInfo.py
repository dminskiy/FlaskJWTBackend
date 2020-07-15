import requests

SERVER_MESSAGES = {
    'repeated_usr': 'The user already exists.'
}

class ServerInfo:
    def __init__(self):
        self.uri = "http://127.0.0.1:5000"

    def get_uri(self):
        return self.uri

    def check_server_connection(self):
        try:
            http_address = self.uri + "/"
            response = requests.get(http_address)
        except:
            return False
        if not response.status_code == 200:
            return False
        return True