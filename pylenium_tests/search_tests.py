from unittest import TestCase
import unittest
from selenium.webdriver.common.keys import Keys

__author__ = 'devgen'

from selenium import webdriver
#
# driver = webdriver.Firefox()
# # driver = None
#
# test_finish = 0
# methods_count = 0
#
#
# def close_firefox():
#     if test_finish >= methods_count:
#         driver.close()
#
#
# class MethodsCounter(type):
#     def __new__(mcs, class_name, bases, class_dict):
#         global methods_count
#         for attrName, attr in class_dict.items():
#             if attrName.startswith("test_"):
#                 methods_count += 1
#         print "Count of test methods:", methods_count


class LastTest(TestCase):
    def test_search_with_result(self):
        # global test_finish
        driver = webdriver.Firefox()
        driver.get("http://lastfm.ru")
        elem = driver.find_element_by_css_selector("input.js-search.search-box")

        elem.send_keys("tool")
        elem.send_keys(Keys.RETURN)

        driver.implicitly_wait(10)

        assert driver.find_element_by_css_selector("#resultsSummary")
        assert driver.find_element_by_css_selector("#topResult")

        # test_finish += 1
        #
        # close_firefox()
        driver.close()

    def test_search_with_no_result(self):
        # global test_finish
        driver = webdriver.Firefox()
        driver.get("http://lastfm.ru")
        elem = driver.find_element_by_css_selector("input.js-search.search-box")

        elem.send_keys("ydf70h78234y78g43nh4uc34rg43rw34io34hu34cg4rh8g2nh")
        elem.send_keys(Keys.RETURN)

        driver.implicitly_wait(10)

        assert driver.find_element_by_css_selector("div.messageBox.errorMessage")

        # test_finish += 1
        #
        # close_firefox()
        driver.close()


if __name__ == '__main__':
    unittest.main()