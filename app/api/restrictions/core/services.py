from app.api.restrictions import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin

class RestrictionService(APIEntityServiceMixin):

    __TABLE_NAME = 'restrictions'
    
    @property
    def _EntityServiceMixin__collection(self):
        return APIDatabaseController(collection)

    def get_with_params(self, params):  #user info
        pass
        # return self.__restrictions_collection.delete(id)