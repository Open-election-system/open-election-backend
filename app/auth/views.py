from flask import request
from flask_restplus import Namespace, Resource, fields

from app.auth import namespace
from app.auth.controllers import AuthController
from app.auth.models import auth, login_response
from app.api.users.models import user, user_response
from app.core.exceptions import EmailInUseException, IncorectCredentials

auth_controller = AuthController()

@namespace.route('/login')
class LoginResource(Resource):

    @namespace.doc('login a user')
    @namespace.expect(auth)
    @namespace.response(200, 'Success', user_response)
    @namespace.response(401, IncorectCredentials.description)
    def post(self):
        """
        login a user.
        """
        data = request.json
        return auth_controller.login(data)
    
    
@namespace.route('/register')
class RegisterResource(Resource):

    @namespace.doc('register a user')
    @namespace.expect(user)
    @namespace.response(200, 'Success', user_response)
    @namespace.response(401, EmailInUseException.description)
    def post(self):
        """
        register a user.
        """
        data = request.json
        return auth_controller.register(data)