from selenium import webdriver
from lastfm.helpers.profile.page import ProfilePage

__author__ = 'devgen'

import unittest
from unittest import TestCase
from lastfm import config


class ProfileTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = ProfilePage(cls.driver)
        cls.page.open(config.PROFILE_URL)

    def test_profile_last_recent(self):
        self.assertTrue(self.page.new_tracks_bar.songs > 0)

    def test_profile_library(self):
        self.assertTrue(self.page.library.artists > 0)

    @classmethod
    def tearDownClass(cls):
        # cls.auth.auth_bar.logout()
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()