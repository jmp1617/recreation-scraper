"""
recreation_gov/park_search

park search associated functions
"""

import recreation_gov.api.park_search_api as api


# take a search query and return a list of possible parks filtered on
# entity type "recarea" and suggested locations
def park_search(search_query: str) -> ({}, {}):
    park_blob, location_blob = api.park_search_request(search_query)
    clean_park_blob, clean_location_blob = {}, {}
    for possible_park in park_blob:
        if possible_park.get("entity_type") == "recarea":
            clean_park_blob[possible_park.get("name")] = possible_park
    for possible_location in location_blob:
        clean_location_blob[possible_location.get("text")] = possible_location
    return clean_park_blob, clean_location_blob
