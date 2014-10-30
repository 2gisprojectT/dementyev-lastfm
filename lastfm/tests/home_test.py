# coding=utf-8
__author__ = 'devgen'

from unittest import TestCase
import unittest
from selenium import webdriver
from lastfm import config
from lastfm.helpers.home.page import HomePage
from lastfm.helpers.auth.page import AuthPage


class HomeTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = HomePage(cls.driver)
        cls.auth = AuthPage(cls.driver)
        cls.page.open(config.S_AUTH_URL)
        cls.auth.auth_bar.login(config.USERNAME, config.PASSWORD)
        # cls.page.open(config.HOME_URL)

    def test_check_recommendations(self):
        self.assertTrue(self.page.recommendation_bar.section())

    def test_check_recommendations_artists(self):
        self.assertTrue(self.page.recommendation_bar.artists())

    def test_check_recommendations_more(self):
        self.assertTrue(self.page.recommendation_bar.more_button())

    def test_check_library(self):
        self.assertTrue(self.page.library_bar.section())

    def test_check_library_numbers(self):
        self.assertTrue(self.page.library_bar.numbers())

    def test_check_library_new_in_library(self):
        self.assertTrue(self.page.library_bar.new())

    @classmethod
    def tearDownClass(cls):
        # cls.auth.auth_bar.logout()
        cls.driver.close()
        pass


if __name__ == '__main__':
    unittest.main()
