
from app.api.core.builders import APIBaseBuilder


class ElectionBuilder(APIBaseBuilder):
    
    @classmethod
    def get_data(cls):
        data_election = data.get('election') if 'election' in data else None 
        data_restrictions = data.get('restrictions') if 'restrictions' in data else None 
        data_options = data.get('options') if 'options' in data else None 
        
    @classmethod
    def build(cls, data):
        data_election, data_restrictions, data_options = cls.get_data()
        restrictions = cls.__build_restrictions(data_restrictions)
        election = cls.__build_election({**data_election, 'restrictions_id': restrictions.id})
        for data_opt in data_options:
            data_opt['elections_id']: election.id
        options = cls.__build_options(data_options)

    @classmethod
    def __build_election(cls, election):
        return container.elections_service.create(election)

    @classmethod
    def __build_restrictions(cls, restrictions):
        default_restrictions = {
            'ageFrom': 18,
            'ageTo': None,
            'votes_number': 1,
            'reatract': False,
            'start': '',  # now
            'end': '',  # now + day
            'organization': None,
        }
        return container.restrictions_service.create({**default_restrictions, **restrictions})

    @classmethod
    def __build_options(options):
        return container.options_service.batch_create(options)