from app.api.core.facades import APIBaseFacade
from app.core.serializers import Serializer
from app.api.elections.serializers import ElectionObject
from app.api.elections.core.iterators import ElectionAgregator

class ElectionFacade(APIBaseFacade):
    
    @classmethod
    def get_elections_by_user_id(cls, user_id):
        from app.api import container
        
        elections = []
        user_info = container.facades.users.get_user_info(user_id)
        available_restrictions = container.services.restrictions().get_by_params(user_info)
        for restrictions in available_restrictions:
            election = container.services.elections().get_by_restriction(restrictions)
            user_votes_number = container.services.votings().count_user_election_votes(election['id'], user_id)
            
            can_vote = container.services.elections().can_user_vote_in_election(restrictions, user_votes_number)
            
            election_obj = ElectionObject(election=election, restrictions=restrictions, votes_number=user_votes_number, can_vote=can_vote)
            serialized_election = Serializer.serialize(election_obj)
            elections.append(serialized_election)
        return elections
    
    @classmethod
    def get_all_elections(cls):
        from app.api import container
        
        elections=[]
        election_list = container.services.elections().get_all()
        for election in election_list:
            options = container.services.options().get_by_election_id(election['id'])
            restrictions = container.services.restrictions().get_by_election_id(election['id'])
            
            election_obj = ElectionObject(election=election, restrictions=restrictions, options=options)
            serialized_election = Serializer.serialize(election_obj)
            elections.append(serialized_election)
        return elections


    @classmethod
    def get_election(cls, election_id, user_id):
        from app.api import container
        
        election = container.services.elections().get_one(str(election_id))
        restrictions = container.services.restrictions().get_by_election_id(election_id)
        user_votes = container.services.votings().get_user_election_votes(election_id, user_id)
        options = container.services.options().get_by_election_id(election_id)
        election_obj = ElectionObject(election=election, restrictions=restrictions, options=options, votes=user_votes)
        serialized_election = Serializer.serialize(election_obj)
        return serialized_election

    @classmethod
    def get_election_stats(cls, election_id):
        election = container.services.elections().get_one(election_id)
        votes_number = container.service.votes().count(election_id)
        options = container.services.options().get_by_election_id(election_id)
        election_obj = ElectionObject(election=election, votes_number=votes_number, options=option)
        serialized_election = Serializer.serialize(election_obj)
        return serialized_election

    @classmethod
    def create_election(cls, data):
        from app.api import container
        return container.builders.elections.build(data)


    @classmethod
    def get_election_stats(cls):
        election_agregator = ElectionAgregator()
        for n in election_agregator: pass # don't remove this line
        serialized_report = Serializer.serialize(election_agregator.report)
        return serialized_report