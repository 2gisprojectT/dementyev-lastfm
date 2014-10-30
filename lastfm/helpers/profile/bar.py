from lastfm.helpers.base_component import BaseComponent

__author__ = 'devgen'


class NewTracksBar(BaseComponent):
    selector = {
        'self': 'div#recentTracks',
        'songs': 'div#recentTracks tr',
    }

    @property
    def songs(self):
        return len(
            self.driver.find_elements_by_css_selector(self.selector['songs'])
        )


class LibraryBar(BaseComponent):
    selector = {
        'self': 'div#taste',
        'artists': 'div#taste ul.libraryItems',
    }

    @property
    def artists(self):
        return len(
            self.driver.find_elements_by_css_selector(self.selector['artists'])
        )
