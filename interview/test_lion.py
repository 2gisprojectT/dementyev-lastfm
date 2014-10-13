# coding=utf-8
from unittest import TestCase
import unittest
from interview import states
from interview.lion import Lion

__author__ = 'devgen'

"""
                Сытый                                       Голодный
Антилопа    |   спать, перейти в состояние голодный     |   съесть, перейти в состояние сытый
Охотник     |   убежать, перейти в состояние голодный   |   убежать
Дерево      |   смотреть, перейти в состояние голодный  |   спать

"""


class TestLion(TestCase):
    def test_lion_correct_init(self):
        lion = Lion()
        self.assertEqual(lion.state.__class__, states.HungryState)

        lion = Lion(states.FedState())
        self.assertEqual(lion.state.__class__, states.FedState)

    def test_lion_incorrect_init(self):
        self.assertRaises(Exception, Lion.__init__, "string")
        self.assertRaises(Exception, Lion.__init__, 1)
        self.assertRaises(Exception, Lion.__init__, states.State())
        self.assertRaises(Exception, Lion.__init__, states.State)

    def test_raise_to_wrong_company(self):
        lion = Lion()

        # wrong input test
        self.assertRaises(Exception, lion.meet, 'tre')

    def test_hungry_lion_meet_hunter(self):
        lion = Lion()

        # now lion is hungry and
        lion.meet('hunter')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['hunter'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['hunter'])

    def test_hungry_lion_meet_tree(self):
        lion = Lion()

        # now lion is hungry and
        lion.meet('tree')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['tree'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['tree'])

    def test_hungry_lion_meet_antelope(self):
        lion = Lion()

        # now lion is hungry and
        lion.meet('antelope')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['antelope'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['antelope'])

    def test_fed_lion_meet_hunter(self):
        lion = Lion(states.FedState())

        # now lion is fed and
        lion.meet('hunter')
        self.assertEqual(lion.reaction, states.FedState().possible_reaction['hunter'])
        self.assertEqual(lion.state.__class__, states.FedState().consequence_state['hunter'])

    def test_fed_lion_meet_tree(self):
        lion = Lion(states.FedState())

        # now lion is fed and
        lion.meet('tree')
        self.assertEqual(lion.reaction, states.FedState().possible_reaction['tree'])
        self.assertEqual(lion.state.__class__, states.FedState().consequence_state['tree'])
