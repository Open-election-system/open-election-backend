from app.api.users import collection
from app.api.elections import collection as election_collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class UserService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'user'
    
    @property
    def _EntityServiceMixin__collection(self):
        return APIDatabaseController(collection)