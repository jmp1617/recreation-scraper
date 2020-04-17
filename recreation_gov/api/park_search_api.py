"""
recreation_gov/api/park_search_api.py

leverage recreation.gov's inventory search api to get a list of
national parks
"""

import recreation_gov.api.meta_api as api


URL = api.BASE_URL + api.PARK_SEARCH_ENDPOINT


# filter on inventory_suggestions to ignore articles and stuff about park
def park_search_request(search_query: str) -> []:
    params = {"q": str(search_query), "geocoder": "true"}
    return api.request(URL, params, api.HEADERS).get("inventory_suggestions")
