from app.api.restrictions import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityService

class RestrictionService(APIEntityService):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)
