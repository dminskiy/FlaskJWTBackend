from random import choice
import string

def generate_string(num_chars):
    letters = string.ascii_letters
    return ''.join(choice(letters) for i in range(num_chars))

class UserClass:
    def __init__(self):
        self.username = generate_string(10)
        self.password = 'test_pass'
        self.items = []

    def add_item(self, item):
        if not item.item_name:
            raise ValueError("Item is missing the content")
        self.items.append(item)

    def login_as_json(self):
        return {
            "username": self.username,
            "password": self.password
        }

class ItemClass:
    def __init__(self):
        self.item_name = generate_string(5)