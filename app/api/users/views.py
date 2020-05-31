from . import namespace
from flask_restplus import Namespace, Resource, fields
from app.api.users.data import USERS
from app.api.users.serializers import user

@namespace.route('/')
class UserList(Resource):
    @namespace.doc('list_users')
    @namespace.marshal_list_with(user)
    def get(self):
        '''List all users'''
        return USERS

@namespace.route('/<id>')
@namespace.param('id', 'The user identifier')
@namespace.response(404, 'User not found')
class User(Resource):
    @namespace.doc('get_user')
    @namespace.marshal_with(user)
    def get(self, id):
        '''Fetch a user given its identifier'''
        for user in USERS:
            if user['id'] == id:
                return user
        namespace.abort(404)