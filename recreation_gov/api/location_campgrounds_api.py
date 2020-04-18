"""
recreation_gov/api/location_campgrounds_api.py

get a list of campsites near a location (not inventory)
"""

import recreation_gov.api.api_helper as api

URL = api.BASE_URL + api.CAMPSITES_ENDPOINT


# filter campgrounds in a defined radius around a location
def extract_sites_location(latitude: str, longitude: str, radius: int) -> []:
    filter_queries = [
        "campsite_type_of_use:Overnight",
        "entity_type:campground"
    ]
    params = {
        "exact": "false",
        "lat": latitude,
        "lng": longitude,
        "radius": str(radius),
        "size": "300",
        "fq": []
    }
    for query in filter_queries:
        params["fq"].append(query)
    response = api.request(URL, params, api.HEADERS)
    return response.get("results")
