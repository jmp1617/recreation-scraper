"""
recreation_gov/api/CampInfo.py

representation of a campground
"""

import recreation_gov.api.camp_info_api as info_api


class CampInfo:
    def __init__(self):
        self.facility_id = 0
        self.facility_name = ""
        self.activities = []
        self.addresses = []
        self.amenities = {}
        self.campsites = []
        self.cancellation = ""
        self.facility_description = {}
        # below sourced by site search
        self.rating = 0.0
        self.number_ratings = 0

    def load_by_id(self, camp_id: int):
        response = info_api.get_camp_info(camp_id)
        self.activities = response.get("activities")
        self.facility_id = camp_id
        self.facility_name = response.get("facility_name")
        self.addresses = response.get("addresses")
        self.amenities = response.get("amenities")
        self.campsites = response.get("campsites")
        self.cancellation = response.get("cancellation_description")
        self.facility_description = response.get("facility_description_map")

    def load_rating(self, rating: str, num_rating: int):
        self.rating = rating
        self.number_ratings = num_rating

    def flush(self):
        self.facility_id = 0
        self.facility_name = ""
        self.activities = []
        self.addresses = []
        self.amenities = {}
        self.campsites = []
        self.cancellation = ""
        self.facility_description = {}
        self.rating = 0.0
        self.number_ratings = 0
