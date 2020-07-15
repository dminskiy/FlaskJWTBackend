from tests.testClasses import TestRegistrationClass
from tests.dbClasses import UserClass

if __name__ == "__main__":
    has_error = False
    test_reg = TestRegistrationClass()
    if not test_reg.server_is_connected():
        has_error = True
        raise ConnectionRefusedError("Could not connect to the server at: {}".format(test_reg.server_uri))
    else:
        print("Success. Connection active with: {}".format(test_reg.server_uri))

    user = UserClass()
    if not test_reg.test_registration(user):
        has_error = True
        print("Error. Registration attempt failed.")
    else:
        print("Success. The user was added to the database: {}".format(user.login_as_json()))

    #TODO: Create a test class for every end point. Global user:UserClass, control its state.
    #TODO: test login
        #TODO: Expected input test
        #TODO: Non-existent user test
        #TODO: Wrong password test
        #TODO: Incomplete input test
        #TODO: Wrong HTTP request type test

    #TODO: test /items/new
        #TODO: Expected input test. Check the item was added to DB. Add more that 1
        #TODO: Incomplete/Wrong token
        #TODO: Wrong input test
        #TODO: Wrong HTTP request type

    #TODO: test /items
        #TODO: Check list against expected
        #TODO: Wrong HTTP request type

    #TODO: test /items/:id
        #TODO: Expected input test. Check the item was deleted from DB
        #TODO: Non-existent id
        #TODO: Incomplete/Wrong token
        #TODO: Wrong HTTP request type


    if has_error:
        print("\nTest failed. Please, see the log")
    else:
        print("\nTest passed. No errors were triggered")