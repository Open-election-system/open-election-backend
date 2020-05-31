from flask_restplus import Namespace, Resource, fields

from . import namespace

@namespace.route('/')
class UserList(Resource):
    @namespace.doc('list_users')
    def get(self):
        '''List all users'''
        return 'hello'
