from app.models.restrictions import collection
from app.models.db_controller.db_controller import DatabaseController
from app.controllers.entity_controller.entity_controller import EntityController


class RestrictionsController(EntityController):
    __restrictions_collection = DatabaseController(collection)

    def get_all(self):
        return self.__restrictions_collection.get_all()

    def get_one(self, id):
        return self.__restrictions_collection.get_one(id)

    def create(self, data):
        return self.__restrictions_collection.post(data)

    def update(self, id, data):
        return self.__restrictions_collection.put(id, data)

    def delete(self, id):
        return self.__restrictions_collection.delete(id)
