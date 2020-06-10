from app.auth import collection as auth_collection
from app.auth.utils import process_user_data
from app.api.users import collection as user_collection
from app.api.locations import collection as location_collection
from app.api.organizations import collection as organization_collection
from app.api.core.controllers.database import APIDatabaseController
from app.auth.core.controllers.database import AuthDatabaseController
from app.auth.core.controllers.entity import AuthEntityController

from app.auth.utils import UserInfo

from app.core.exceptions import EmailInUseException, IncorectCredentials

class AuthController(AuthEntityController):
    
    __auth_collection = AuthDatabaseController(auth_collection)
    __user_collection = APIDatabaseController(user_collection)
    __location_collection = APIDatabaseController(location_collection)
    __organization_collection = APIDatabaseController(organization_collection)

    
    def register(self, data):
        cls = self.__class__
        # # pick email from the request json
        # email_filter = {cls.EMAIL: data[cls.EMAIL]}
        credentials, user_info, location, job = process_user_data(data)
        # Check if users with the same email already exist:
        query_documents = self.__auth_collection.filter_equal_values(credentials)
        if len(query_documents) > 0: raise EmailInUseException()
        id = self.__auth_collection.post(credentials)

        find_location = self.__location_collection.filter_equal_values(location)
        location_id = self.__location_collection.post(location) if len(find_location) == 0 else list(find_location)[0]

        find_job = self.__organization_collection.filter_equal_values(job)
        job_id = self.__organization_collection.post(job) if len(find_job) == 0 else list(find_job)[0]

        user_info.update({UserInfo.LOCATION_ID.value: location_id})
        user_info.update({UserInfo.ORGANIZATION_ID.value: job_id})
        return self.__user_collection.post(user_info, id=id)
    
    def login(self, data):
        cls = self.__class__
        query_documents = self.__auth_collection.filter_equal_values(data)
        # Another way to query data is:
        # query_documents = self.__auth_collection.filter_any_values([{
        #     "parameter": cls.EMAIL,
        #     "sign": u"==",
        #     "value": "string"
        # }])
        
        # check if the query result is empty and raise an error:
        if len (query_documents) == 0: raise IncorectCredentials()
        id = list(query_documents)[0]
        user_model = dict(list(self.__user_collection.get_one(id))[0])
        user_model.update(query_documents[id])
        return user_model
