__author__ = 'devgen'

import states


class Lion(object):
    def __init__(self):
        self.state = states.HungryState()
        self.reaction = 'born'

    def meet(self, company):
        # self.state = self.state.conversate(company)
        for attr, value in self.state.conversate(company).viewitems():
            setattr(self, attr, value)

    def status(self):
        print "Lion is", self.reaction, "and feel", self.state



