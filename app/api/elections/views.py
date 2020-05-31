from . import namespace
from flask_restplus import Namespace, Resource, fields
from app.api.elections.data import ELECTIONS
from app.api.elections.serializers import election

@namespace.route('/')
class ElectionList(Resource):
    @namespace.doc('list_elections')
    @namespace.marshal_list_with(election)
    def get(self):
        '''List all elections'''
        return ELECTIONS

@namespace.route('/<id>')
@namespace.param('id', 'The election identifier')
@namespace.response(404, 'Election not found')
class Election(Resource):
    @namespace.doc('get_election')
    @namespace.marshal_with(election)
    def get(self, id):
        '''Fetch a election given its identifier'''
        for election in ELECTIONS:
            if election['id'] == id:
                return election
        namespace.abort(404)