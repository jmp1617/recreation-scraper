"""
recreation_gov/ParkSearch.py

park search associated functions
holds search state
"""

import recreation_gov.api.park_search_api as api


class ParkSearch:
    def __init__(self):
        self.parks = {}
        self.locations = {}
        self.search_query = ""

    # take a search query and return a list of possible parks filtered on
    # entity type "recarea" and suggested locations
    def load_search(self, search_query: str):
        self.search_query = search_query
        park_blob, location_blob = api.park_search_request(search_query)
        for possible_park in park_blob:
            if possible_park.get("entity_type") == "recarea":
                self.parks[possible_park.get("name")] = possible_park
        for possible_location in location_blob:
            self.locations[possible_location.get("text")] = possible_location

    def get_park_results(self) -> {}:
        return self.parks

    def get_location_results(self) -> {}:
        return self.locations

    def flush(self):
        self.parks = {}
        self.locations = {}
        self.search_query = ""
