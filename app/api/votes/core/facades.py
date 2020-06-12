
from app.api.core.facades import APIBaseFacade


class VotingFacade(APIBaseFacade):
    
    @classmethod
    def vote_by_user(cls, id):
        from app.api import container
        vote = container.services.votings().get_one(id)
        print(vote)
    