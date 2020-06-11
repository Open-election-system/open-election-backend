from flask import request
from flask_restplus import Resource

from app.api.users import namespace

from app.api.users.models import user, user_response


@namespace.route('')
class UserList(Resource):
    @namespace.doc('list_users')
    @namespace.marshal_list_with(user)
    def get(self):
        """
        Get all users.
        """
        from app.api import container
        return container.services.restrictions().get_all()

    @namespace.doc('add_user')
    @namespace.expect(user)
    @namespace.response(200, 'Success', user_response)
    def post(self):
        """
        Create a new user.
        """
        data = request.json
        from app.api import container
        return container.services.restrictions().create(data)


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
        from app.api import container
        return container.services.restrictions().get_one(id)

    @namespace.doc('update_user')
    @namespace.expect(user)
    def update(self, id):
        """
        Update existing user.
        """
        data = request.json
        from app.api import container
        return container.services.restrictions().update(id, data)

    def delete(self, id):
        """
        Delete existing user.
        """
        from app.api import container
        return container.services.restrictions().delete(id)
