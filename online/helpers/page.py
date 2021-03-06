class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._extras_bar = None
        self._route_bar = None

    @property
    def search_bar(self):
        from online.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from online.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def extras_bar(self):
        from online.helpers.extras_bar import ExtrasBar

        if self._extras_bar is None:
            self._extras_bar = ExtrasBar(self.driver, self.driver.find_element_by_css_selector(ExtrasBar.selectors['extras_button']))
        return self._extras_bar

    @property
    def route_bar(self):
        from online.helpers.route_bar import RouteBar

        if self._route_bar is None:
            self._route_bar = RouteBar(self.driver, self.driver.find_element_by_css_selector(RouteBar.selectors['route']))
        return self._route_bar

    def open(self, url):
        self.driver.get(url)

