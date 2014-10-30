from lastfm.helpers.page import Page

__author__ = 'devgen'


class AuthPage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self._auth_bar = None
        self._auth_result = None

    @property
    def auth_bar(self):
        from lastfm.helpers.auth.bar import AuthBar

        if self._auth_bar is None:
            self._auth_bar = AuthBar(
                element=self.driver.find_element_by_css_selector(AuthBar.selector['self']),
                driver=self.driver,
            )
        return self._auth_bar

    @property
    def auth_result(self):
        from lastfm.helpers.auth.result import AuthResult

        if self._auth_result is None:
            self._auth_result = AuthResult(
                element=self.driver.find_element_by_css_selector(AuthResult.selector['user_button']),
                driver=self.driver,
            )
        return self._auth_result