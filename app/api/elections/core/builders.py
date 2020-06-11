
from app.api.core.builders import APIBaseBuilder


class ElectionBuilder(APIBaseBuilder):
    
    @classmethod
    def get_data(cls, data):
        data_election = data.get('election') if 'election' in data else None 
        data_restrictions = data.get('restrictions') if 'restrictions' in data else None 
        data_options = data.get('options') if 'options' in data else None 
        return data_election, data_restrictions, data_options
        
    @classmethod
    def build(cls, data):
        data_election, data_restrictions, data_options = cls.get_data(data)
        election = cls.__build_election(data_election)
        restrictions = cls.__build_restrictions({ **data_restrictions, 'election_id': election})
        for data_opt in data_options:
            data_opt['election_id'] = election
        options = cls.__build_options(data_options)
        return 'Success'

    @classmethod
    def __build_election(cls, election):
        from app.api import container
        return container.services.elections().create(election)

    @classmethod
    def __build_restrictions(cls, restrictions):
        from app.api import container
        default_restrictions = {
            'age_from': 18,
            'age_to': None,
            'votes_number': 1,
            'reatract': False,
            'start': '',  # now
            'end': '',  # now + day
            'organization': None,
        }
        return container.services.restrictions().create({**default_restrictions, **restrictions})

    @classmethod
    def __build_options(cls, options):
        from app.api import container
        return container.services.options().batch_create(options)