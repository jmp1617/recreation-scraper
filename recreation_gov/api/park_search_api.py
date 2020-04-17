"""
recreation_gov/api/park_search_api.py

leverage recreation.gov's inventory search api to get a list of
national parks and suggested locations
"""

import recreation_gov.api.meta_api as api


URL = api.BASE_URL + api.PARK_SEARCH_ENDPOINT


# filter on inventory_suggestions and suggestions to ignore articles and stuff about park
def park_search_request(search_query: str) -> ([], []):
    params = {"q": str(search_query), "geocoder": "true"}
    response = api.request(URL, params, api.HEADERS)
    parks = response.get("inventory_suggestions")
    locations = response.get("suggestions")
    return parks, locations
