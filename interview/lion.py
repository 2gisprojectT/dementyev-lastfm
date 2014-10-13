__author__ = 'devgen'

import states


class Lion(object):
    def __init__(self, state=states.HungryState()):
        if state.__class__ and state.__class__.__base__ is states.State:
            self.state = state
            self.reaction = 'sleep'
        else:
            raise Exception("Lion cannot take this state")

    def meet(self, company):
        # self.state = self.state.conversate(company)
        for attr, value in self.state.conversate(company).viewitems():
            setattr(self, attr, value)

    def status(self):
        print "Lion is", self.reaction, "and feel", self.state



