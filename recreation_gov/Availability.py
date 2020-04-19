"""
recreation_gov/Availability.py

Availability associated functions
"""

import recreation_gov.api.availability_api as availability


def format_time(start_date: str, end_date: str) -> (str, str):
    return start_date + "T00:00:00Z", end_date + "T00:00:00Z"


class Availability:
    def __init__(self):
        self.targets = []
        # date format yyyy-mm-dd
        self.start_date = ""
        self.end_date = ""

    def add_target_campground(self, park_id: int):
        self.targets.append(park_id) if self.targets.count(park_id) == 0 else 0

    def set_target_window(self, start_date: str, end_date: str):
        self.start_date, self.end_date = format_time(start_date, end_date)

    # ignores detail, if an availability is found, short circuits returning value
    def get_availability_fast(self) -> (int, bool):
        if len(self.targets) == 0 or len(self.start_date) == 0 or len(self.end_date) == 0:
            print("Insufficient data for availability check...")
        else:
            results = []
            for target in self.targets:
                ava = str(availability.get_site_availability(target, self.start_date, self.end_date))
                if "\'Available\'" in ava or "\"Available\"" in ava:
                    return [(target, True)]
                else:
                    results.append((target, False))
            return results

    # returns the parent park, site number, max occupants as well
    def get_availability_detail(self) -> (int, int, int, bool):
        if len(self.targets) == 0 or len(self.start_date) == 0 or len(self.end_date) == 0:
            print("Insufficient data for availability check...")
        else:
            results = []
            for target in self.targets:
                new_additions = 0
                response = availability.get_site_availability(target, self.start_date, self.end_date)
                for site in response.values():
                    ava = str(site.get("availabilities").get(self.start_date))
                    if ava == "Available":
                        results.append((target, int(site.get("campsite_id")), int(site.get("max_num_people")), True))
                        new_additions -= -1
                if new_additions == 0:
                    results.append((target, 0, 0, False))
            return results
