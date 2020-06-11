from app.api.core.facades import APIBaseFacade

class ElectionFacade(APIBaseFacade):
    
    @classmethod
    def get_elections(cls, user_id):
        from app.api import container
        
        elections = []
        user_info = container.facades.users.get_user_info(user_id)
        available_restrictions = container.services.restrictions().get_by_params(user_info)
        for restriction in available_restrictions:
            election = container.services.elections().get_by_restriction(restriction)
            user_votes_number = container.services.votings().count_user_election_votes(election['id'], user_id)
            
            can_vote = container.services.elections().can_user_vote_in_election(restriction, user_votes_number)
            
            elections.append({'election': election, 'restrictions': restriction, 'votes_number': user_votes_number, 'can_vote': can_vote})
        return elections

    @classmethod
    def get_election(cls, election_id, user_id):
        from app.api import container
        election = container.services.elections().get_one(str(election_id))
        print(election)
        restrictions = container.services.restrictions().get_by_equal_params({'election_id': election_id})
        print(restrictions)
        user_votes = container.services.votings().get_user_election_votes(election_id, user_id)
        print(user_votes)
        options = container.services.options().get_by_election(election_id)
        print("options", options)
        election = {'election': election, 'restrictions': restrictions, 'votes': user_votes, 'options': options}
        return election

    @classmethod
    def get_election_stats(cls, election_id):
        election = container.services.elections().get_one(election_id)
        voteYs_number = container.service.votes().count(election_id)
        options = container.services.options().get_by_election(election_id)
        election = {'election': election, 'votes_number': votes_number, 'options': options}
        return election

    @classmethod
    def create_election(cls, data):
        return container.election_builder.build(data)
