from app.api.restrictions import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin

class RestrictionService(APIEntityServiceMixin):

    __TABLE_NAME = 'restrictions'
    
    @property
    def _EntityServiceMixin__collection(self):
        return APIDatabaseController(collection)

    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
    
    def get_with_params(self, params):  #user info
        """
            default_restrictions = {
                'ageFrom': 18,
                'ageTo': None,
                'votes_number': 1,
                'reatract': False,
                'start': '',  # now
                'end': '',  # now + day
                'organization': None,
            }
        """
        pass