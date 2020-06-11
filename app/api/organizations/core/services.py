from app.api.organizations import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin


class OrganizationService(APIEntityServiceMixin):
    
    __TABLE_NAME = 'organizations'
    
    @property
    def _EntityServiceMixin__collection(self):
        """
            Warning: don't change a name of the function.
        """
        return APIDatabaseController(collection)
    
    @property
    def __collection(self):
        return self._EntityServiceMixin__collection

    def get_by_organization_id(self, organization_id):
        organization = self.__collection.get_one(organization_id)
        return organization[0]
    