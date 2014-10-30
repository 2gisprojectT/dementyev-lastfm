from lastfm.helpers.base_component import BaseComponent

__author__ = 'devgen'


class RecommendationBar(BaseComponent):
    selector = {
        'self': 'section.artist-grid.artist-grid--g8.artist-grid--logged-in-home',
        'artists': 'ul.artist-grid-items.clearit',
        'more': 'a.btn.btn--block',
    }

    def section(self):
        return self.driver.find_element_by_css_selector(self.selector['self'])

    def artists(self):
        return self.driver.find_element_by_css_selector(self.selector['artists'])

    def more_button(self):
        return self.driver.find_element_by_css_selector(self.selector['more'])


class LibraryBar(BaseComponent):
    selector = {
        'self': 'div.g4',
        'numbers': 'div.g4 ul.r.library-numbers',
        'new': 'div.g4 ul.r.recent-artists'
    }

    def section(self):
        return self.driver.find_element_by_css_selector(self.selector['self'])

    def numbers(self):
        return self.driver.find_element_by_css_selector(self.selector['numbers'])

    def new(self):
        return self.driver.find_element_by_css_selector(self.selector['new'])


