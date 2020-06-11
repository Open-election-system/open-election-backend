from app.api.votes import collection

from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityService


class VotingService(APIEntityService):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)
        
        