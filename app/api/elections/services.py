from app.api.elections import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityService


class ElectionService(APIEntityService):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)
