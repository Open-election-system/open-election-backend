
from app.core.services.entity.firestore import EntityServiceMixin
from app.api.core.controllers.database import APIDatabaseController

class APIEntityServiceMixin(EntityServiceMixin):

    __collection = APIDatabaseController('root')
