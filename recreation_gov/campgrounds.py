"""
recreation_gov/campgrounds.py

campground extractor associated functions
"""

import recreation_gov.api.campgrounds_api as inventory
import recreation_gov.api.location_campgrounds_api as location


# return list of campgrounds. most specific using rec_gov inventory system id
def get_inventory_sites(park_id: int) -> []:
    return inventory.extract_sites_park(park_id)


# return list of campgrounds. more relaxed search based on geo loc
def get_location_sites(latitude: str, longitude: str, radius: int) -> []:
    radius = 500 if radius > 500 else radius
    return location.extract_sites_location(latitude, longitude, radius)
