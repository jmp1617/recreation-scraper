
"""
campspotter.py

TUI for recreation.gov with cancellation notifications via text
"""


def print_usage():
    print("USAGE: campspotter.py")


class Campspotter:
    def __init__(self):
        self.advanced_mode = False
        self.selected_park = "None"
        self.selected_site_name = "None"
        self.selected_start_date = "None"
        self.selected_end_date = "None"
        self.watching = []
        self.selected_site_id = -1

    def display_header(self):
        print("Campspotter v1.0\n")
        print("Selected Park: ", self.selected_park)
        print("Selected Site: ", self.selected_site_name)
        print("Start Date: ", self.selected_start_date)
        print("End Date: ", self.selected_end_date)
        print("Watch List: "),
        counter = len(self.watching)
        if counter == 0:
            print("Empty")
        else:
            for site in self.watching:
                print(site),
                if counter != 1:
                    print(", ")
                counter -= 1
            print()
