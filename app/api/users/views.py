from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields

from app.api.users import namespace, collection
from app.api.users.data import USERS
from app.api.users.serializers import user

@namespace.route('')
class UserList(Resource):
    @namespace.doc('list_users')
    @namespace.marshal_list_with(user)
    def get(self):
        """
            read() : Fetches documents from Firestore collection as JSON.
            user : Return document that matches query ID.
        """
        try:
            all_users = [doc.to_dict() for doc in collection.stream()]
            return jsonify(all_users), 200
        except Exception as e:
            return f"An Error Occured: {e}"

    @namespace.doc('add_user')
    @namespace.expect(user)
    def post(self):
        """
        Creates a new user.
        """
        id = request.json.get('id')
        collection.document(str(id)).set(request.json)
        return None, 201

@namespace.route('/<id>')
@namespace.param('id', 'The user identifier')
@namespace.response(404, 'User not found')
class User(Resource):
    @namespace.doc('get_user')
    @namespace.marshal_with(user)
    def get(self, id):
        """
            get() : Fetches documents from Firestore collection as JSON.
            user : Return document that matches query ID.
        """
        try:
            if id:
                user = collection.document(id).get()
                if user.exists:
                    
                    return jsonify(user.to_dict()), 200
                else:
                    raise FileNotFoundError 
        except Exception as e:
            return f"An Error Occured: {e}"
    
    @namespace.doc('update_user')
    @namespace.expect(user)
    def update(self):
        """
        Creates a new user.
        """
        id = request.json.get('id')
        collection.document(str(id)).update(request.json)
        return None, 201