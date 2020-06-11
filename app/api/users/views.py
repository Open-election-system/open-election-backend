from flask import request
from flask_restplus import Resource

from app.api.users import namespace, user_info_namespace

from app.api.users.models import user, user_response, user_info, user_info_response, user_full_info


@namespace.route('')
class UserList(Resource):
    @namespace.doc('list_users')
    @namespace.marshal_list_with(user_full_info)
    def get(self):
        """
        Get all users.
        """
        from app.api import container
        return container.facades.users().get_all()

    @namespace.doc('add_user')
    @namespace.response(200, 'Success', user_response)
    def post(self):
        """
        Create a new user.
        """
        data = request.json
        from app.api import container
        # return container.services.users().create(data)
        return container.facades.users.create_user(data)


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
        return container.services.users().get_one(id)

    @namespace.doc('update_user')
    @namespace.expect(user)
    def put(self, id):
        """
        Update existing user.
        """
        data = request.json
        from app.api import container
        return container.services.users().update(id, data)

    def delete(self, id):
        """
        Delete existing user.
        """
        from app.api import container
        return container.services.users().delete(id)


# USER INFO


@user_info_namespace.route('')
class UserInfoList(Resource):

    @user_info_namespace.doc('add user info')
    @user_info_namespace.expect(user_info)
    @user_info_namespace.response(200, 'Success', user_info_response)
    def post(self):
        """
        Add user info
        """
        data = request.json
        from app.api import container
        return container.services.user_info().create(data)
    
@user_info_namespace.route('/<id>')
@user_info_namespace.param('id', 'The user identifier')
@user_info_namespace.response(404, 'User info not found')
class UserInfo(Resource):
    
    @user_info_namespace.marshal_list_with(user_info_response)
    @user_info_namespace.response(200, 'Success', user_info_response)
    @user_info_namespace.doc('get_user_info')
    def get(self, id):
        """
        Get a user info by user id.
        """
        from app.api import container
        return container.services.user_info().get_one(id)

    @user_info_namespace.doc('update_user_info')
    @user_info_namespace.expect(user_info)
    def put(self, id):
        """
        Update existing user info by user id.
        """
        data = request.json
        from app.api import container
        return container.services.user_info().update(id, data)

    def delete(self, id):
        """
        Delete existing user info by user id.
        """
        from app.api import container
        return container.services.user_info().delete(id)
