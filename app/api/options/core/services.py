from app.api.options import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class OptionService(APIEntityServiceMixin):

    __TABLE_NAME = 'options'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)

    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
    
    def get_by_election(self, election_id):
        pass
        # return self.__options_collection.get_one(id)