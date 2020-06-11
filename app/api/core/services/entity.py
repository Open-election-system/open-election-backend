
from app.core.services.entity.firestore import EntityService
from app.api.core.controllers.database import APIDatabaseController

class APIEntityService(EntityService):

    __collection = APIDatabaseController('root')
