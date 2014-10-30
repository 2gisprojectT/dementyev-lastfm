from lastfm.helpers.page import Page

__author__ = 'devgen'


class ProfilePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self._new_tracks_bar = None
        self._library_bar = None

    @property
    def new_tracks_bar(self):
        from lastfm.helpers.profile.bar import NewTracksBar

        if self._new_tracks_bar is None:
            self._new_tracks_bar = NewTracksBar(
                element=self.driver.find_element_by_css_selector(NewTracksBar.selector['self']),
                driver=self.driver,
            )
        return self._new_tracks_bar

    @property
    def library(self):
        from lastfm.helpers.profile.bar import LibraryBar

        if self._library_bar is None:
            self._library_bar = LibraryBar(
                element=self.driver.find_element_by_css_selector(LibraryBar.selector['self']),
                driver=self.driver,
            )
        return self._library_bar