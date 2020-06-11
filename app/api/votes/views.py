from flask import request
from flask_restplus import Resource

from app.api.votes import namespace
from app.api.votes.models import vote,vote_response



@namespace.route('')
class VotingList(Resource):
    @namespace.doc('list_votes')
    @namespace.marshal_list_with(vote)
    def get(self):
        """
        Get all votes.
        """
        from app.api import container
        return container.services.votings().get_all()

    @namespace.doc('add_vote')
    @namespace.expect(vote)
    @namespace.response(200, 'Success', vote_response)
    def post(self):
        """
        Create a new vote.
        """
        data = request.json
        from app.api import container
        return container.services.votings().create(data)


@namespace.route('/<id>')
@namespace.param('id', 'The vote identifier')
@namespace.response(404, 'Voting not found')
class Voting(Resource):
    @namespace.doc('get_vote')
    def get(self, id):
        """
        Get a vote by id.
        """
        # vote_col = db.collection('vote')
        # voting_col = db.collection('votings')
        # votes = vote_service.get_many_to_many(vote_col, voting_col, voteId=id, votingId=None)
        from app.api import container
        return container.services.votings().get_one(id)

    @namespace.doc('update_vote')
    @namespace.expect(vote)
    def put(self, id):
        """
        Update existing vote.
        """
        data = request.json
        from app.api import container
        return container.services.votings().update(id, data)

    def delete(self, id):
        """
        Delete existing vote.
        """
        from app.api import container
        return container.services.votings().delete(id)
