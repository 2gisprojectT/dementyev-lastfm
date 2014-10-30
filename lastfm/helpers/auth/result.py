from lastfm.helpers.base_component import BaseComponent

__author__ = 'devgen'


class AuthResult(BaseComponent):

    selector = {
        'user_button': 'a.btn.btn--small.btn--header.user-badge',
        'enter_button': 'a#login-link',
    }

    def user(self):
        return self.driver.find_element_by_css_selector(self.selector['user_button']).get_attribute('href').split('/')[-1]

    def login_button(self):
        return self.driver.find_element_by_css_selector(self.selector['enter_button'])