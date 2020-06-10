container = {}


class ElectionsBuilder:
    @staticmethod
    def build(data):
        data_election = data.get('election')
        data_restrictions = data.get('restrictions')
        data_options = data.get('options')

        restrictions = ElectionsBuilder.__build_restrictions(data_restrictions)
        election = ElectionsBuilder.__build_election({**data_election, 'restrictions_id': restrictions.id})
        for data_opt in data_options:
            data_opt['elections_id']: election.id
        options = ElectionsBuilder.__build_options(data_options)

    @staticmethod
    def __build_election(election):
        return container.elections_service.create(election)

    @staticmethod
    def __build_restrictions(restrictions):
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

    @staticmethod
    def __build_options(options):
        return container.options_service.batch_create(options)