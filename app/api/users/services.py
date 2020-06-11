from app.api.users import collection
from app.api.elections import collection as election_collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityService


class UserService(APIEntityService):

    @property
    def _EntityService__collection(self):
        return APIDatabaseController(collection)

# # Facade pattern

# class UserMakerController(APIEntityService):
    
#     __users_collection = APIDatabaseController(collection)
#     __elections_collection = APIDatabaseController(election_collection)

#     def get_all_user_elections(self, data):
#         if 'election_id' in request.args:
#             param = int(request.args.get('election_id'))
#             print(param)
        
        