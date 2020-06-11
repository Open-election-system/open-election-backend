import datetime

from app.api.restrictions import collection
from app.api.core.controllers.database import APIDatabaseController
from app.api.core.services.entity import APIEntityServiceMixin
from app.api.restrictions.data import default_restrictions


class RestrictionService(APIEntityServiceMixin):

    __TABLE_NAME = 'restrictions'

    @property
    def _EntityServiceMixin__collection(self):
        return APIDatabaseController(collection)

    @property
    def __collection(self):
        return self._EntityServiceMixin__collection

    def get_by_params(self, params):  # user info
        """
            default_restrictions = {
                'age_from': 18,
                'age_to': None,
                'votes_number': 1,
                'reatract': False,
                'start': '',  # now
                'end': '',  # now + day
                'organization': None,
            }
        """
        age = int(params['age'])
        organization = params['organization']
        election_id = params['user_id']
        time_now = datetime.datetime.now().timestamp()

        query_result = self.__collection.get_by_params_alternately([
            # age
            {
                "parameter": 'age_from',
                "sign": u"<=",
                "value": age
            },
            {
                "parameter": 'age_to',
                "sign": u">=",
                "value": age
            },
            # time
            {
                "parameter": 'start',
                "sign": u"<=",
                "value": time_now
            },
            {
                "parameter": 'end',
                "sign": u">=",
                "value": time_now
            },
            # organization
            {
                "parameter": 'organization',
                "sign": u"==",
                "value": organization
            },
        ])

        
        # TODO get votes number and check with reatract

        # from app.api import container
        # container.services.votings().get_by_equal_params({'election_id':election_id, 'user_id':user_id})
        # available_restrictions = query_result
        return query_result
    

    def get_by_election_id(self, election_id):
        from app.api import container
        return container.services.restrictions().get_by_equal_params({'election_id': election_id})
