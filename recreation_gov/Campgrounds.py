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

    # loads list of campgrounds. most specific using rec_gov inventory system id
    def load_inventory_sites(self, park_id: int):
        self.sites = inventory.extract_sites_park(park_id)

    # loads list of campgrounds. more relaxed search based on geo loc
    def load_location_sites(self, latitude: str, longitude: str, radius: int):
        radius = 500 if radius > 500 else radius
        self.sites = location.extract_sites_location(latitude, longitude, radius)

    def flush(self):
        self.sites = []

