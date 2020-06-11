from flask import request
from flask_restplus import Resource

from app.api.elections import namespace
from app.api.elections.models import election, election_response, election_full_model, election_user_response_model,  election_full_response_model

parser = namespace.parser()
parser.add_argument('user-id', help='user id', required=False, location='headers')

@namespace.route('')
@namespace.expect(parser)
class ElectionList(Resource):
    
    @namespace.doc('list elections')
    @namespace.expect(parser)
    @namespace.marshal_list_with(election_user_response_model)
    @namespace.response(200, 'Success', election_user_response_model)
    def get(self):
        """
        Get all elections.
        """
        from app.api import container
        
        user_id = request.headers['user-id'] if 'user-id' in request.headers else None
        if user_id is not None:
            return container.facades.elections.get_elections(user_id)
        else:
            return container.services.elections().get_all()
    
    @namespace.doc('add ele ction')
    @namespace.expect(election)
    def post(self):
        """
        Create a new election.
        """
        data = request.json
        from app.api import container
        return container.services.elections().create(data)


@namespace.route('/all/')
class ElectionListAll(Resource):
    
    @namespace.doc('list elections')
    @namespace.marshal_list_with(election_full_response_model)
    @namespace.response(200, 'Success', election_full_response_model)
    def get(self):
        """
        Get all elections.
        """
        from app.api import container
        
        return container.facades.elections().get_all_elections()
        
@namespace.route('/<int:id>')
@namespace.expect(parser)
@namespace.param('id', 'The election identifier')
@namespace.response(404, 'election not found')
class Election(Resource):
    
    @namespace.doc('get_election')
    @namespace.response(200, 'Success', election_response)
    def get(self, election_id):
        """
        Get an election by id.
        """
        # user_id = request.headers['user-id']
        # return container.elections_facade.get_election(election_id, user_id)
        from app.api import container
        return container.services.elections().get_one(election_id)

    @namespace.doc('update_election')
    @namespace.expect(election)
    def put(self, election_id):
        """
        Update existing election.
        """
        data = request.json
        # return container.elections_facade.create_election(data)
        from app.api import container
        return container.services.elections().update(election_id, data)

    def delete(self, election_id):
        """
        Delete existing election.
        """
        from app.api import container
        return container.services.elections().delete(election_id)


@namespace.route('/stats/<id>')
@namespace.expect(parser)
@namespace.param('id', 'The election identifier')
class ElectionStats(Resource):
    @namespace.doc('get_election')
    def get(self, election_id):
        """
        Get a election by id.
        """
        # user_id = request.headers['user-id']
        from app.api import container
        # return container.elections_facade.get_election(election_id)
