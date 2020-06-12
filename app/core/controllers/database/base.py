import abc

class BaseDatabaseController:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_one(self, id):
        pass

    @abc.abstractmethod
    def post(self, id, data):
        pass

    @abc.abstractmethod
    def put(self, id, data):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def batch_create(self, id):
        pass