from tests.ServerInfo import ServerInfo, SERVER_MESSAGES
import requests

class TestRegistrationClass:
    def __init__(self):
        self.server = ServerInfo()
        self.server_uri = self.server.get_uri()
        self.reg_uri = self.server_uri + "/registration"
        self.users_uri = self.server_uri + "/users"

    def server_is_connected(self):
        return self.server.check_server_connection()

    def test_registration(self, user):
        response = self.init_registration(user)

        if not self.check_registration_is_correct(response, user):
            return False

        if not self.check_is_repeated_user(user):
            return False

        if not self.check_faulty_user():
            return False

        if not self.check_wrong_http_method(user):
            return False

        return True

    def check_wrong_http_method(self, user):
        response = self.init_registration(user, "get")
        if response.status_code == 405:
            return True
        else:
            print("Error. Wrong HTTP method test failed. Unexpected HTTP Status code: {}. Expected: 400".format(response.status_code))
            return False

    def check_faulty_user(self):
        http_address = self.reg_uri
        user_json = {"username": "test"}
        try:
            response = requests.post(http_address, user_json)
        except:
            print("Error. Faulty user test failed. Cannot access the server.")
            return False
        if response.status_code == 400:
            return True
        else:
            print("Error. Faulty user test failed. Unexpected HTTP Status code: {}. Expected: 400".format(response.status_code))
            return False

    def check_is_repeated_user(self, user):
        response = self.init_registration(user)
        if response.status_code == 400 and response.json()["msg"] == SERVER_MESSAGES["repeated_usr"]:
            return True
        else:
            print("Error. Repeated user check has failed: {}".format(user.login_as_json()))
            return False

    def check_registration_is_correct(self, response, user):
        if not response:
            print("Error. Cannot access /registration endpoint")
            return False

        if response.status_code != 200:
            print("Error. Could not register a user: {}".format(user.login_as_json()))
            return False

        user_is_in_db = self.isInDatabase(user)
        if user_is_in_db == None:
            print("Error. /registration HTTP Status: 200. Cannot access the server.")

        if not user_is_in_db:
            print("Error. /registration HTTP Status: 200 but cannot find user in the database: {}".format(
                user.login_as_json()))
            return False

        return True

    def init_registration(self, user, method="post"):

        if method == "post":
            response = self.register_correctly(user)
        else:
            if method == "get":
                response = requests.get(self.reg_uri)
            else:
                import sys
                raise ValueError("Error in {} Only [post, get] methods are available.".format(sys._getframe().f_code.co_name))

        return response

    def register_correctly(self, user):
        try:
            http_address = self.reg_uri
            response = requests.post(http_address, json=user.login_as_json())
            return response
        except:
            return None

    def isInDatabase(self, user):
        try:
            http_address = self.users_uri
            response = requests.get(http_address)
            if response.status_code != 200:
                return None
            response = response.json()
            for db_user in response["data"]["users"]:
                if db_user["username"] == user.username and db_user["password"] == user.password:
                    return True
            return False
        except:
            return None