"""
recreation_gov/Campgrounds.py

campground extractor associated functions
holds campsite results in state
"""

import recreation_gov.api.campgrounds_api as inventory
import recreation_gov.api.location_campgrounds_api as location


class Campgrounds:
    def __init__(self):
        self.sites = []
        self.load_method = ""

    # loads list of campgrounds. most specific using rec_gov inventory system id
    def load_inventory_sites(self, park_id: int):
        self.load_method = "inventory"
        self.sites = inventory.extract_sites_park(park_id)

    # loads list of campgrounds. more relaxed search based on geo loc
    def load_location_sites(self, latitude: str, longitude: str, radius: int):
        self.load_method = "location"
        radius = 500 if radius > 500 else radius
        self.sites = location.extract_sites_location(latitude, longitude, radius)

    def get_site_results(self) -> []:
        return self.sites

    def flush(self):
        self.sites = []
        self.load_method = ""
