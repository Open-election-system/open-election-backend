from flask import request
from flask_restplus import Resource

from app.api.users import namespace
from app.api.users.models import user
from app.api.users.controllers import UserController

user_controller = UserController()


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
    def post(self):
        """
        Create a new user.
        """
        data = request.json
        return user_controller.create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The user identifier')
@namespace.response(404, 'User not found')
class User(Resource):
    @namespace.doc('get_user')
    def get(self, id):
        """
        Get a user by id.
        """
        # vote_col = db.collection('vote')
        # voting_col = db.collection('votings')
        # votes = user_controller.get_many_to_many(vote_col, voting_col, userId=id, votingId=None)
        return user_controller.get_one(id)

    @namespace.doc('update_user')
    @namespace.expect(user)
    def update(self, id):
        """
        Update existing user.
        """
        data = request.json
        return user_controller.update(id, data)

    def delete(self, id):
        """
        Delete existing user.
        """
        return user_controller.delete(id)
