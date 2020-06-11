from app.api.options import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityService


class OptionService(APIEntityService):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)
