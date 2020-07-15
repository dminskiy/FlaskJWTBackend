from bson import ObjectId
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

import app.database.mongo_service as svc

unPswdParser = reqparse.RequestParser()
unPswdParser.add_argument('username', help='The required field.', required = True)
unPswdParser.add_argument('password', help='The required field.', required = True)

itemParser = reqparse.RequestParser()
itemParser.add_argument('item_name', help = 'The required field.', required = True)

class UserRegistration(Resource):
    def post(self):
        data = unPswdParser.parse_args()

        user = svc.find_user_by_username(data["username"])

        if user:
            return {'msg': 'The user already exists.'}, 400

        try:
            svc.add_new_user(data["username"], data["password"])
            return {'msg': 'User registration successful.'}, 200
        except:
            return {'msg': 'Could not add a new user. Check DB connection.'}, 400

class UserLogin(Resource):
    def post(self):
        data = unPswdParser.parse_args()

        current_user = svc.find_user_by_username(data["username"])

        if not current_user:
            return {'msg' : "This user doesn't exist: {}.".format(data["username"])}

        if current_user.password == data["password"]:
            access_token = create_access_token(identity=data['username'])
            return {
                    'msg': 'Login successful. Logged as {}.'.format(data["username"]),
                    'access_token': access_token
                    }, 200
        else:
            return {'msg': 'Login failed. Wrong credentials.'}, 400

class AllUsers(Resource):
    def get(self):
        all_users = svc.get_all_users()
        return {
                'msg': 'List of users.',
                'data': all_users
                }
    def delete(self):
        num_deleted = svc.delete_all_users()
        return {'msg': 'All {} Users were deleted.'.format(num_deleted)}

class ListUserObjects(Resource):
    @jwt_required
    def get(self):
        current_user = svc.find_user_by_username(get_jwt_identity())
        if not current_user:
            return {'msg': 'Could not find the user: {}.'.format(get_jwt_identity())}, 404

        items = svc.get_all_items(current_user)

        return {
                'msg': 'List of all items. User: {}.'.format(current_user.username),
                'data': items
                }, 200

class DeleteUserObject(Resource):
    @jwt_required
    def delete(self, id):
        current_user = svc.find_user_by_username(get_jwt_identity())
        if not current_user:
            return {'msg': 'Could not find the user: {}.'.format(get_jwt_identity())}, 404

        if svc.isValidItem(current_user, str(id)):
            if svc.delete_item(current_user, str(id)):
                return {'msg': 'Item successfully deleted: {}'.format(id)}, 200
            else:
                return {'msg': 'Could not delete item. DB error: {}'.format(id)}, 200
        else:
            return {'msg': 'Item {} was not found in the record of user {}.'.format(id, current_user.username)}, 404


class AddUserObject(Resource):
    @jwt_required
    def post(self):
        data = itemParser.parse_args()

        current_user = svc.find_user_by_username(get_jwt_identity())

        if not current_user:
            return {'msg': "Could not find the user: {}.".format(get_jwt_identity())}, 400

        item_id = svc.add_item_to_user(current_user, data["item_name"], ObjectId())

        return {
                    'msg': 'An item was added to user: {}.'.format(current_user.username),
                    'item': {
                        '_id': item_id,
                        'item_name': data["item_name"]
                    }
                }, 200

class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            "user": get_jwt_identity(),
            "secret": 777
        }

class ConnectionTest(Resource):
    def get(self):
        return {'msg': 'Connection is OK'}, 200