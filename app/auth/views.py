from flask import request
from flask_restplus import Namespace, Resource, fields

from app.auth import namespace
from app.auth.services import AuthService
from app.auth.models import auth, login_response, error
from app.api.users.models import user, user_response
from app.core.exceptions import EmailInUseException, IncorectCredentials

auth_service = AuthService()

@namespace.route('/login')
class LoginResource(Resource):

    @namespace.doc('login a user')
    @namespace.expect(auth)
    @namespace.response(200, 'Success', user_response)
    @namespace.response(401, IncorectCredentials.description, error)
    def post(self):
        """
        login a user.
        """
        data = request.json
        return auth_service.login(data)
    
    
@namespace.route('/register')
class RegisterResource(Resource):

    @namespace.doc('register a user')
    @namespace.expect(user)
    @namespace.response(200, 'Success', user_response)
    @namespace.response(401, EmailInUseException.description, error)
    def post(self):
        """
        register a user.
        """
        data = request.json
        return auth_service.register(data)