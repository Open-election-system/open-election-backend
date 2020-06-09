from app.auth import collection as auth_collection
from app.api.users import collection as user_collection
from app.api.core.controllers.database import APIDatabaseController
from app.auth.core.controllers.database import AuthDatabaseController
from app.auth.core.controllers.entity import AuthEntityController

from app.core.exceptions import EmailInUseException, IncorectCredentials

class AuthController(AuthEntityController):
    
    __auth_collection = AuthDatabaseController(auth_collection)
    __user_collection = APIDatabaseController(user_collection)

    EMAIL = 'email'
    PASSWORD = 'password'
    
    def register(self, data):
        cls = self.__class__
        # pick email from the request json
        email_filter = {cls.EMAIL: data[cls.EMAIL]}
        # Check if users with the same email already exist:
        query_documents = self.__user_collection.filter_equal_values(email_filter)
        if len(query_documents) > 0: raise EmailInUseException()
        return self.__user_collection.post(data)
    
    def login(self, data):
        cls = self.__class__
        query_documents = self.__user_collection.filter_equal_values(data)
        
        # Another way to query data is:
        # query_documents = self.__auth_collection.filter_any_values([{
        #     "parameter": cls.EMAIL,
        #     "sign": u"==",
        #     "value": "string"
        # }])
        
        # check if the query result is empty and raise an error:
        if len (query_documents) == 0: raise IncorectCredentials()
        user_model = list(query_documents.values())[0]
        return user_model
