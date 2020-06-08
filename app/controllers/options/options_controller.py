from app.models.options import collection
from app.models.db_controller.db_controller import DatabaseController
from app.controllers.entity_controller.entity_controller import EntityController


class OptionsController(EntityController):
    __options_collection = DatabaseController(collection)

    def get_all(self):
        return self.__options_collection.get_all()

    def get_one(self, id):
        return self.__options_collection.get_one(id)

    def create(self, data):
        return self.__options_collection.post(data)

    def update(self, id, data):
        return self.__options_collection.put(id, data)

    def delete(self, id):
        return self.__options_collection.delete(id)
