"""
recreation_gov/api/camp_info_api.py

get info on a specific campsite via rec_gov entity id
"""

import recreation_gov.api.api_helper as api

URL = api.BASE_URL + api.CAMP_INFO_ENDPOINT


def get_camp_info(camp_id: int) -> []:
    return api.request(URL + str(camp_id), {}, api.HEADERS).get("campground")
