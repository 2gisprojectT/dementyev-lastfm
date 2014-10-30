from lastfm.helpers.page import Page

__author__ = 'devgen'


class HomePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self._recommendation_bar = None
        self._library_bar = None

    @property
    def recommendation_bar(self):
        from lastfm.helpers.home.bar import RecommendationBar

        if self._recommendation_bar is None:
            self._recommendation_bar = RecommendationBar(
                element=self.driver.find_element_by_css_selector(RecommendationBar.selector['self']),
                driver=self.driver,
            )
        return self._recommendation_bar

    @property
    def library_bar(self):
        from lastfm.helpers.home.bar import LibraryBar

        if self._library_bar is None:
            self._library_bar = LibraryBar(
                driver=self.driver,
                element=self.driver.find_element_by_css_selector(LibraryBar.selector['self']),
            )
        return self._library_bar