from app import resources

def api_activate_resources(api):
    api.add_resource(resources.UserRegistration, '/registration')
    api.add_resource(resources.UserLogin, '/login')
    api.add_resource(resources.ListUserObjects, '/items')
    api.add_resource(resources.AddUserObject, '/items/new')
    api.add_resource(resources.DeleteUserObject, '/items/<string:id>')

    api.add_resource(resources.ConnectionTest, '/')
    api.add_resource(resources.AllUsers, '/users')
    api.add_resource(resources.SecretResource, '/secret')