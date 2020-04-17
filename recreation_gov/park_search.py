"""
recreation_gov/park_search

park search associated functions
"""

import recreation_gov.api.park_search_api as api


# take a search query and return a list of possible parks filtered on
# entity type "recarea"
def park_search(search_query: str) -> {}:
    park_blob = api.park_search_request(search_query)
    clean_blob = {}
    for possible_park in park_blob:
        if possible_park.get("entity_type") == "recarea":
            clean_blob[possible_park.get("name")] = possible_park
    return clean_blob
