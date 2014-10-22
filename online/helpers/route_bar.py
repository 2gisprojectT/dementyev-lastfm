from online.helpers.base_component import BaseComponent

__author__ = 'devgen'


class RouteBar(BaseComponent):

    selectors = {
        'route': 'div.searchBar__tab.searchBar__rsTab',
        'from': 'div.suggest._module_suggestRs._route_from._placeholder input',
        'to': 'div.suggest._module_suggestRs._route_to._placeholder input',
        'form': 'form.searchBar__form',
        'result': 'header.routeResults__header'
    }

    def search(self, place_from, place_to):
        self.driver.find_element_by_css_selector(self.selectors['route']).click()

        self.driver.find_element_by_css_selector(self.selectors['from']).send_keys(place_from)
        self.driver.find_element_by_css_selector(self.selectors['to']).send_keys(place_to)

        self.driver.find_element_by_css_selector(self.selectors['form']).submit()

    def result(self):
        return self.driver.find_element_by_css_selector(self.selectors['result'])
