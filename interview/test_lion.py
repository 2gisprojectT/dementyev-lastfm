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
    def test_meet(self):
        lion = Lion()

        # now lion is hungry and
        lion.meet('hunter')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['hunter'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['hunter'])

        # now lion is hungry and
        lion.meet('tree')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['tree'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['tree'])

        # lion is hungry and
        lion.meet('antelope')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['antelope'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['antelope'])

        # now lion is fed and
        lion.meet('hunter')
        self.assertEqual(lion.reaction, states.FedState().possible_reaction['hunter'])
        self.assertEqual(lion.state.__class__, states.FedState().consequence_state['hunter'])

        # lion is hungry and
        lion.meet('antelope')
        self.assertEqual(lion.reaction, states.HungryState().possible_reaction['antelope'])
        self.assertEqual(lion.state.__class__, states.HungryState().consequence_state['antelope'])

        # now lion is fed and
        lion.meet('tree')
        self.assertEqual(lion.reaction, states.FedState().possible_reaction['tree'])
        self.assertEqual(lion.state.__class__, states.FedState().consequence_state['tree'])

    def test_raise(self):
        lion = Lion()

        # wrong input
        self.assertRaises(Exception, lion.meet, 'bla')
