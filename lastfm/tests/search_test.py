# coding=utf-8
from unittest import TestCase
import unittest
from selenium import webdriver
from unittest_data_provider import data_provider
from lastfm.helpers.search.page import SearchPage

import lastfm.config as config

__author__ = 'devgen'


class SearchTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = SearchPage(cls.driver)
        cls.page.open(config.SEARCH_URL)

    bad_data = lambda: (
        ('2390g2uh0evw',),
        ('ne0rg0ge00jn',),
        (u'3y7b§¶¶∫¨∫ˆ˙',),
    )

    good_data = lambda: (
        ('arctic monkeys',),
        ('radioactive',),
        ('y.o.u',),
    )

    @data_provider(good_data)
    def test_search_good(self, query):
        self.page.search_bar.search(query)
        self.assertTrue(self.page.search_result.yes())

    @data_provider(bad_data)
    def test_search_bad(self, query):
        self.page.search_bar.search(query)
        self.assertTrue(self.page.search_result.no())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()