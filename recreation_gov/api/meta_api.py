"""
recreation_gov/api/meta_api.py

constants for all api requests
"""
from fake_useragent import UserAgent
import requests

# UNIVERSAL
BASE_URL = "https://www.recreation.gov/api"

# ENDPOINTS (GET)
PARK_SEARCH_ENDPOINT = "/search/suggest"
CAMPSITES_ENDPOINT = "/search/geo"
CAMP_INFO_ENDPOINT = "/camps/campgrounds/"  # requires a campsite ID in URL
AVAILABILITY_ENDPOINT = "/camps/availability/campground/"  # requires a campsite ID in URL

# BASE HEADER
HEADERS = {"User-Agent": UserAgent().random}


# SKELETON REQUEST
def request(url: str, params: {str: str}, header: {str: str}) -> {}:
    response = requests.get(url, params=params, headers=header)
    if response.status_code != 200:
        raise RuntimeError(
            "failedRequest",
            "ERROR, {} code recieved from {}: {}".format(
                response.status_code, url, response.text
            )
        )
    return response.json()
