from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields

from app.api.controller import Controller

from app.api.users import namespace, collection
from app.api.users.models import user
from app.api.controller import Controller


user_controller = Controller(collection)

@namespace.route('')
class UserList(Resource):
    @namespace.doc('list_users')
    @namespace.marshal_list_with(user)
    def get(self):
        """
        Get all users.
        """
        return user_controller.get_all()

    @namespace.doc('add_user')
    @namespace.expect(user)
    def post(self):
        """
        Create a new user.
        """
        id = request.json.get('id')
        data = request.json
        return user_controller.post(id, data)


@namespace.route('/<id>')
@namespace.param('id', 'The user identifier')
@namespace.response(404, 'User not found')
class User(Resource):
    @namespace.doc('get_user')
    @namespace.marshal_with(user)
    def get(self, id):
        """
        Get a user by id.
        """
        return user_controller.get_one(id)
    
    @namespace.doc('update_user')
    @namespace.expect(user)
    def update(self, id):
        """
        Update existing user.
        """
        data = request.json
        return user_controller.put(id, data)

    def delete(self, id):
        """
        Delete existing user.
        """
        return user_controller.delete(id)