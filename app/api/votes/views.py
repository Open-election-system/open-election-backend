from flask import request
from flask_restplus import Resource

from app.api.votes import namespace
from app.api.votes.models import vote
from app.api.votes.services import VotingService

vote_service = VotingService()


@namespace.route('')
class VotingList(Resource):
    @namespace.doc('list_votes')
    @namespace.marshal_list_with(vote)
    def get(self):
        """
        Get all votes.
        """
        return vote_service.get_all()

    @namespace.doc('add_vote')
    def post(self):
        """
        Create a new vote.
        """
        data = request.json
        return vote_service.create(data)


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
        return vote_service.get_one(id)

    @namespace.doc('update_vote')
    @namespace.expect(vote)
    def update(self, id):
        """
        Update existing vote.
        """
        data = request.json
        return vote_service.update(id, data)

    def delete(self, id):
        """
        Delete existing vote.
        """
        return vote_service.delete(id)
