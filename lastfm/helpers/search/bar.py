from lastfm.helpers.base_component import BaseComponent

__author__ = 'devgen'


class SearchBar(BaseComponent):
    selector = {
        'self': 'form#search',
        'input': 'input#search_query',
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selector['input']).clear()
        self.driver.find_element_by_css_selector(self.selector['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selector['self']).submit()