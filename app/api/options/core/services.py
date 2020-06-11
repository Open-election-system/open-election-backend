from app.api.options import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class OptionService(APIEntityServiceMixin):

    __TABLE_NAME = 'options'

    @property
    def _EntityServiceMixin__colection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)

    @property
    def __collection(self):
        return self._EntityServiceMixin__colection

    def get_by_election(self, election_id):
        return self.__collection.get_by_equal_params({'election_id': int(election_id)})
