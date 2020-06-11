from flask import request
from flask_restplus import Resource

from app.api.elections import namespace
from app.api.elections.models import election

@namespace.route('')
class ElectionList(Resource):
    @namespace.doc('list elections')
    @namespace.marshal_list_with(election)
    def get(self):
        """
        Get all elections.
        """
        # user_id = request.headers['user-id']
        # return container.elections_facade.get_elections(user_id)
        from app.api import container
        return container.services.elections().get_all()

    @namespace.doc('add election')
    @namespace.expect(election)
    def post(self):
        """
        Create a new election.
        """
        data = request.json
        from app.api import container
        return container.services.elections().create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The election identifier')
@namespace.response(404, 'election not found')
class Election(Resource):
    @namespace.doc('get_election')
    def get(self, election_id):
        """
        Get a election by id.
        """
        # user_id = request.headers['user-id']
        # return container.elections_facade.get_election(election_id, user_id)
        from app.api import container
        return container.services.elections().get_one(election_id)

    @namespace.doc('update_election')
    @namespace.expect(election)
    def update(self, election_id):
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
