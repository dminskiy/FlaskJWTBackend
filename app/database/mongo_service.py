import mongoengine
from bson import ObjectId

from app.database.models import User, Item

def mongo_global_init(config):
    print("Connecting to DB: {}".format(config.MONGODB_NAME))
    try:
        db = mongoengine.connect(alias=config.MONGODB_ALIAS, name=config.MONGODB_NAME)
        objects = User.objects()
        if not objects:
            raise RuntimeError("Can't connect to the database. MongoDB server can't be reached.")
        return db
    except:
        raise RuntimeError("Can't connect to the database.")

def add_new_user(username: str, password: str) -> User:
    new_user = User()
    new_user.username = username
    new_user.password = password

    new_user.save()
    return new_user

def find_user_by_username(username: str) -> User:
    user = User.objects(username=username).first()
    return user

def add_item_to_user(user: User, item_name: str, id: ObjectId) -> str:
    item = Item()
    item._id = str(id)
    item.item_name = item_name
    user.items.append(item)
    user.save()

    return item._id

def item_to_json(itm):
    return{
        "_id":itm._id,
        "item_name": itm.item_name
    }

def usr_to_json(usr, full = True):
    if full:
        return {
                "_id": str(usr.pk),
                "username": usr.username,
                "password": usr.password,
                'items': list(map(lambda x: item_to_json(x), usr.items))
                }
    else:
        return {'items': list(map(lambda x: item_to_json(x), usr.items))}

def get_all_users():
    return {'users': list(map(lambda x: usr_to_json(x), User.objects()))}

def get_all_items(usr: User):
    return usr_to_json(usr, False)

def delete_all_users():
    total_objects = User.objects.count()
    User.objects.delete()
    return total_objects

def isValidItem(usr: User, id: str) -> bool:
    if usr.items.filter(_id=id).first():
        return True
    return False

def delete_item(usr: User, id: str) -> bool:
    try:
        usr.items.filter(_id = id).delete()
        usr.save()
        return True
    except:
        import sys
        raise ValueError("Error: {}".format(sys.exc_info()))
        return False