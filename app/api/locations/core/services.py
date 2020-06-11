from app.api.locations import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class LocationService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'locations'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)
    
    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
    
    def get_by_location_id(self, location_id):
        location = self.__collection.get_one(location_id)
        return location[0]
    