import mongoengine
from bson import ObjectId

class Item(mongoengine.EmbeddedDocument):
    item_name = mongoengine.StringField(required=True)
    _id = mongoengine.StringField(default=str(ObjectId()), primary_key=True)

class User(mongoengine.Document):
    username = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)

    items = mongoengine.EmbeddedDocumentListField(Item)

    meta = {
        'db_alias': 'default',
        'collection': 'users'
    }