"""
recreation_gov/api/availability_api.py

availability at campsite id per date
"""

import recreation_gov.api.api_helper as api

URL = api.BASE_URL + api.AVAILABILITY_ENDPOINT


def get_site_availability(camp_id: int, start_date: str, end_date: str) -> {}:
    params = {
        "start_date": start_date,
        "end_date": end_date
    }
    return api.request(URL + str(camp_id), params, api.HEADERS).get("campsites")
