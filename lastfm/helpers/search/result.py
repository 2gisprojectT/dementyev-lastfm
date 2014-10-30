from lastfm.helpers.base_component import BaseComponent

__author__ = 'devgen'


class SearchResult(BaseComponent):
    selector = {
        'success': 'div#resultsSummary',
        'failed': 'div#noResults'
    }

    def yes(self):
        return self.driver.find_element_by_css_selector(self.selector['success'])

    def no(self):
        return self.driver.find_element_by_css_selector(self.selector['failed'])
