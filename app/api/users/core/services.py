from app.api.users import collection, user_info_collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class UserService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'user'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)
    
    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
    
    
class UserInfoService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'user_info'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(user_info_collection)
    
    @property
    def __collection(self):
        return self._EntityServiceMixin__collection
    
    @classmethod
    def get_table_name(cls):
        return cls.__TABLE_NAME
    
    
    def get_by_user_id(self, user_id):
        user_info = self.__collection.get_by_equal_params({'user_id': int(user_id)})
        return user_info[0]
    