from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from online.helpers.base_component import BaseComponent

__author__ = 'devgen'


class ExtrasBar(BaseComponent):

    selectors = {
        'extras_button': '.extras__btn.extras__share',
        'share_popup_output': 'input.share__popupUrlInput',
    }

    def extract(self):
        self.driver.find_element_by_css_selector(self.selectors['extras_button']).click()
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_css_selector(self.selectors['share_popup_output']).get_attribute('value')



