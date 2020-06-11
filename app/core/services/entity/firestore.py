import abc

from app.core.services.entity.base import BaseEntityService
from app.core.controllers.database.firestore import DatabaseController

class EntityServiceMixin(BaseEntityService):
    """
        This class is not an instance of BaseEntityService cause it doesn't implement __colection property.
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

    def filter_equal_values(self, id, filter_dict):
        return self.__collection.filter_equal_values(filter_dict)

    def filter_any_values(self, filter_list):
        return self.__collection.filter_any_values(filter_list)
