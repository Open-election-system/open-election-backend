from app.api.elections import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class ElectionService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'election'
    
    @property
    def _EntityServiceMixin__collection(self):
        return APIDatabaseController(collection)
