from app.api.locations import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.controllers.entity import APIEntityController


class LocationController(APIEntityController):
    __locations_collection = APIDatabaseController(collection)

    def get_all(self):
        return self.__locations_collection.get_all()

    def get_one(self, id):
        return self.__locations_collection.get_one(id)

    def create(self, data):
        return self.__locations_collection.post(data)

    def update(self, id, data):
        return self.__locations_collection.put(id, data)

    def delete(self, id):
        return self.__locations_collection.delete(id)

    def batch_create(self, id):
        return self.__locations_collection.batch_create(id)
