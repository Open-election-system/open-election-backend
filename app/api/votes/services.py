from app.api.votes import collection

from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class VotingService(APIEntityServiceMixin):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)
        
        