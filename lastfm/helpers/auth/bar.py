from lastfm.helpers.base_component import BaseComponent

__author__ = 'devgen'


class AuthBar(BaseComponent):
    selector = {
        'self': 'div#loginForm form',
        'login': 'input#username',
        'pass': 'input#password',
        'logout': 'li form input.dropdown-btn-menu-item.logout-button',
        'drop_menu': 'a.user-dropdown-toggle.btn.btn--small.btn--header.btn--icon-only.needs-js.iconright.iconright--dropdown.menu-toggle',
    }

    def login(self, username, password):
        self.driver.find_element_by_css_selector(self.selector['login']).send_keys(username)
        self.driver.find_element_by_css_selector(self.selector['pass']).send_keys(password)
        self.driver.find_element_by_css_selector(self.selector['self']).submit()

    def logout(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(self.selector['drop_menu']).click()
        self.driver.find_element_by_css_selector(self.selector['logout']).click()


