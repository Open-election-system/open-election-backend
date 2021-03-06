import abc

from app.core.services.entity.base import BaseEntityService
from app.core.controllers.database.firestore import DatabaseController

class EntityServiceMixin(BaseEntityService):
    """
        This class can't inherit BaseEntityService cause it doesn't implement __colection property.
        So, we call it a Mixin. (read python mixins)
    """
    def get_one(self, id):
        return self.__collection.get_many_to_many(id)
      
    def get_many_to_many(self, id):
        return self.__collection.get_many_to_many(id)

    def get_all(self):
        return self.__collection.get_all()

    def get_one(self, id):
        return self.__collection.get_one(id)

    def create(self, data):
        return self.__collection.post(data)

    def batch_create(self, data_list):
        return self.__colection.batch_create(data_list)
     
    def update(self, id, data):
        return self.__collection.put(id, data)

    def get_by_equal_params(self, filter_dict):
        return self.__collection.get_by_equal_params(filter_dict)

    def get_by_any_params(self, filter_list):
        return self.__collection.get_by_any_params(filter_list)