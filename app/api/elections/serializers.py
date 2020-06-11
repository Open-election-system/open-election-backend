


class ElectionObject:
    
    def __init__(self, election, restrictions=[], votes_number=0, can_vote=False, options=[], votes=[]):
        self.election = election
        self.restriction = restrictions
        self.votes_number = votes_number
        self.can_vote = can_vote
        self.options = options
        self.votes = votes