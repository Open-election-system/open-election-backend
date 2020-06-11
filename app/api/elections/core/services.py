from app.api.elections import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class ElectionService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'election'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)

    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
    
    
    def get_by_restriction(self, restriction):
        election_id = restriction['election_id']
        available_election = self.__collection.get_by_equal_params({'id': int(election_id)})[0]
        return available_election
    
    def can_user_vote_in_election(self, restriction, user_votes_number):
        reatract = False
        if restriction['votes_number'] == 0:
            if restriction['votes_number'] < user_votes_number:
                reatract = True
        elif bool(restriction['reatract']):
                reatract = True      
        return reatract