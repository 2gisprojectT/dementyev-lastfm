__author__ = 'devgen'


class State(object):
    """ Abstract class """

    def __init__(self):
        pass

    def conversate(self, company):
        if company in self.possible_reaction:
            # print self.possible_reaction[company], '=>', 'Get', self.consequence_state[company].__name__
            # return self.consequence_state[company]()
            return {
                'reaction': self.possible_reaction[company],
                'state': self.consequence_state[company]()
            }
        raise Exception("Life of lion is not ready to " + company)


class HungryState(State):
    def __init__(self):
        super(HungryState, self).__init__()
        self.possible_reaction = {
            'antelope': 'eat antelope',
            'hunter': 'run away',
            'tree': 'sleep',
        }
        self.consequence_state = {
            'antelope': FedState,
            'hunter': HungryState,
            'tree': HungryState,
        }

    def __str__(self):
        return "hungry"


class FedState(State):
    def __init__(self):
        super(FedState, self).__init__()
        self.possible_reaction = {
            'antelope': 'sleep',
            'hunter': 'run away',
            'tree': 'look, very interesting tree',
        }
        self.consequence_state = {
            'antelope': HungryState,
            'hunter': HungryState,
            'tree': HungryState,
        }

    def __str__(self):
        return "fed"
