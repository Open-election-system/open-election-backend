from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields

from app.api.controller import Controller

from app.api.users import namespace, collection
from app.api.users.models import user
from app.api.controller import Controller

from app import db


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
    def get(self, id):
        """
        Get a user by id.
        """
        vote_col = db.collection('vote')
        voting_col = db.collection('votings')
        votes = user_controller.get_many_to_many(vote_col, voting_col, userId=id, votingId=None)
        return {'user': user_controller.get_one(id), 'votes':votes}
    
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