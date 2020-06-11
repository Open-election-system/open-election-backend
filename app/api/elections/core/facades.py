from app.api.core.facades import APIBaseFacade

class ElectionFacade(APIBaseFacade):
    
    @classmethod
    def get_elections(cls, user_id):
        from app.api import container
        
        elections = []
        user_info = container.facades.users.get_user_info(user_id)
        print(user_info)
        # available_restrictions = container.services.restrictions().get_with_params(user_info)
        # for restriction in available_restrictions:
        #     election = container.services.elections().get_by_restrictions(restriction.id)
        #     user_votes_count = container.services.votings().count(election.id, user_id)
        #     elections.append({'election': election, 'restrictions': restriction, 'votes_count': user_votes_count})
        return elections

    @classmethod
    def get_election(cls, election_id, user_id):
        election_item = container.elections_service.get_one(election_id)
        restrictions = container.restrictions_service.get_one(election_item.restrictions_id)
        user_votes = container.vote_service.get_by_params(election_id, user_id)
        options = container.options_service.get_by_election(election_id)
        election = {'election': election_item, 'restrictions': restrictions, 'votes': user_votes, 'options': options}
        return election

    @classmethod
    def get_election_stats(cls, election_id):
        election_item = container.elections_service.get_one(election_id)
        votes_count = container.vote_service.count(election_id)
        options = container.options_service.get_by_election(election_id)
        election = {'election': election_item, 'votes_count': votes_count, 'options': options}
        return election

    @classmethod
    def create_election(cls, data):
        return container.election_builder.build(data)
