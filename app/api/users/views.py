from flask import request
from flask_restplus import Resource

from app.api.users import namespace

from app.api.users.models import user, user_response
from app.api.users.services import UserService


user_service = UserService()
# user_maker = UserMakerController()

@namespace.route('')
class UserList(Resource):
    @namespace.doc('list_users')
    @namespace.marshal_list_with(user)
    def get(self):
        """
        Get all users.
        """
        return user_service.get_all()

    @namespace.doc('add_user')
    @namespace.expect(user)
    @namespace.response(200, 'Success', user_response)
    def post(self):
        """
        Create a new user.
        """
        data = request.json
        return user_service.create(data)


@namespace.route('/<id>')
@namespace.doc(params={'election_id': {'description': 'The election id'}})
@namespace.param('id', 'The user identifier')
@namespace.response(404, 'User not found')
class User(Resource):
    @namespace.doc('get_user')
    def get(self, id):
        """
        Get a user by id.
        """
        # elections = user_maker.get_all_user_elections(request)
        # print(request.args)
        # vote_col = db.collection('vote')
        # voting_col = db.collection('votings')
        # votes = user_service.get_many_to_many(vote_col, voting_col, userId=id, votingId=None)
        return user_service.get_one(id)

    @namespace.doc('update_user')
    @namespace.expect(user)
    def update(self, id):
        """
        Update existing user.
        """
        data = request.json
        return user_service.update(id, data)

    def delete(self, id):
        """
        Delete existing user.
        """
        return user_service.delete(id)
