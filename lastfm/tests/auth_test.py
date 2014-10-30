import unittest
from selenium import webdriver
from lastfm.helpers.auth.page import AuthPage
from unittest_data_provider import data_provider

__author__ = 'devgen'

from unittest import TestCase
import lastfm.config as config


class AuthTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = AuthPage(cls.driver)
        cls.page.open(config.AUTH_URL)

    users = lambda: (
        (config.USERNAME, config.PASSWORD,),
    )

    @data_provider(users)
    def test_step_a_login(self, username, password):
        self.page.auth_bar.login(username, password)
        self.assertEqual(self.page.auth_result.user(), username)

    def test_step_b_logout(self):
        self.page.auth_bar.logout()
        self.assertTrue(self.page.auth_result.login_button())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()