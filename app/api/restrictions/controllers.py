from app.api.restrictions import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.controllers.entity import APIEntityController

class RestrictionController(APIEntityController):
    __restrictions_collection = APIDatabaseController(collection)

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
