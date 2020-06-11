from app.api.votes import collection

from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class VotingService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'votes'
    
    @property
    def _EntityServiceMixin__collection(self):
        return APIDatabaseController(collection)
        
    def count_by_option(self, option_id):
        pass
        # return self.__votes_collection.delete(id)

    def count_user_election_votes(self, election_id, user_id):
        pass
        # return self.__votes_collection.delete(id)
