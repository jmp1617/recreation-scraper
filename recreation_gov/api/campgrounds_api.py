"""
recreation_gov/api/campground_api.py

get a list of campsites at the inventory park location.
Uses entity id.
"""

import recreation_gov.api.api_helper as api

URL = api.BASE_URL + api.CAMPSITES_ENDPOINT


# filter on campground
def extract_sites_park(park_id: int) -> []:
    filter_queries = [  # filter types of entities returned for a park
        "campsite_type_of_use:Overnight",
        "entity_type:campground",
        "parent_asset_id:"+str(park_id)
    ]
    params = {
        "entity_id": str(park_id),
        "entity_type": "recarea",
        "exact": "false",
        "fq": []
    }
    for query in filter_queries:
        params["fq"].append(query)
    response = api.request(URL, params, api.HEADERS)
    return response.get("results")
