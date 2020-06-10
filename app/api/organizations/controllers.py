from app.api.organizations import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.controllers.entity import APIEntityController


class OrganizationController(APIEntityController):
    __organizations_collection = APIDatabaseController(collection)

    def get_all(self):
        return self.__organizations_collection.get_all()

    def get_one(self, id):
        return self.__organizations_collection.get_one(id)

    def create(self, data):
        return self.__organizations_collection.post(data)

    def update(self, id, data):
        return self.__organizations_collection.put(id, data)

    def delete(self, id):
        return self.__organizations_collection.delete(id)

    def batch_create(self, id):
        return self.__organizations_collection.batch_create(id)
