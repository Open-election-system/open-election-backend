from app.api.votes import collection

from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class VotingService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'votes'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)

    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
        
    def count_by_option(self, option_id):
        pass
        # return self.__votes_collection.delete(id)

    def get_user_election_votes(self, election_id, user_id):
        query_result = self.__collection.get_by_params_alternately([
            {
                "parameter": 'election_id',
                "sign": u"==",
                "value": int(election_id)
            },
            {
                "parameter": 'user_id',
                "sign": u"==",
                "value": int(user_id)
            },
        ])
        return query_result
    
    def count_user_election_votes(self, election_id, user_id):
        query_result = self.get_user_election_votes(election_id, user_id)
        count = len(query_result)
        return count