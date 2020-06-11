from app.api.core.facades import APIBaseFacade

container = {}


class ElectionFacade(APIBaseFacade):
    
    @staticmethod
    def get_elections(user_id):
        elections = []
        user_info = container.users_facade.get_user_info(user_id)
        available_restrictions = container.restrictions_service.get_with_params(user_info)
        for restriction in available_restrictions:
            election = container.elections_service.get_by_restrictions(restriction.id)
            user_votes_count = container.vote_service.count(election.id, user_id)
            elections.append({'election': election, 'restrictions': restriction, 'votes_count': user_votes_count})
        return elections

    @staticmethod
    def get_election(election_id, user_id):
        election_item = container.elections_service.get_one(election_id)
        restrictions = container.restrictions_service.get_one(election_item.restrictions_id)
        user_votes = container.vote_service.get_by_params(election_id, user_id)
        options = container.options_service.get_by_election(election_id)
        election = {'election': election_item, 'restrictions': restrictions, 'votes': user_votes, 'options': options}
        return election

    @staticmethod
    def get_election_stats(election_id):
        election_item = container.elections_service.get_one(election_id)
        votes_count = container.vote_service.count(election_id)
        options = container.options_service.get_by_election(election_id)
        election = {'election': election_item, 'votes_count': votes_count, 'options': options}
        return election

    @staticmethod
    def create_election(data):
        return container.election_builder.build(data)
