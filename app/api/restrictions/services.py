from app.api.restrictions import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin

class RestrictionService(APIEntityServiceMixin):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)
