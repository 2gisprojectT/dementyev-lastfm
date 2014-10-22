# -*- coding:UTF-8 -*-
from unittest import TestCase
import unittest

from selenium import webdriver

from online.helpers.page import Page


class SeleniumTest(TestCase):
    def test_search(self):
        driver = webdriver.Firefox()
        page = Page(driver)

        page.open("http://2gis.ru")

        test_query = u'кафе'
        page.search_bar.search(test_query)

        page.open(page.extras_bar.extract())
        self.assertEqual(test_query, page.search_bar.query())

        driver.close()

    def test_route(self):
        driver = webdriver.Firefox()
        page = Page(driver)

        page.open("http://2gis.ru")

        query_from = u'студенческая'
        query_to = u'золотая нива'

        driver.implicitly_wait(10)
        page.route_bar.search(query_from, query_to)

        driver.implicitly_wait(10)
        self.assertTrue(page.route_bar.result())

        driver.close()


if __name__ == '__main__':
    unittest.main()
