from app.api.options import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.controllers.entity import APIEntityController


class OptionsController(APIEntityController):
    __options_collection = APIDatabaseController(collection)

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

    def batch_create(self, id):
        return self.__options_collection.batch_create(id)
