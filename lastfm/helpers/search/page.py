from lastfm.helpers.page import Page

__author__ = 'devgen'


class SearchPage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self._search_bar = None
        self._search_result = None

    @property
    def search_bar(self):
        from lastfm.helpers.search.bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(
                element=self.driver.find_element_by_css_selector(SearchBar.selector['self']),
                driver=self.driver,
            )
        return self._search_bar

    @property
    def search_result(self):
        from lastfm.helpers.search.result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(
                driver=self.driver,
                element=None,
            )
        return self._search_result