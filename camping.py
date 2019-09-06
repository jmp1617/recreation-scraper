#!/usr/bin/env python3

import argparse
import json
import logging
import sys
from datetime import datetime, timedelta
from twilio.rest import Client

import requests
from fake_useragent import UserAgent

site_found = False

account_sid = ''
auth_token = ''

BASE_URL = "https://www.recreation.gov"
AVAILABILITY_ENDPOINT = "/api/camps/availability/campground/"
MAIN_PAGE_ENDPOINT = "/api/camps/campgrounds/"

INPUT_DATE_FORMAT = "%Y-%m-%d"

headers = {"User-Agent": UserAgent().random}
desired_sites = [232447]
desired_weekends = [["2019-10-11","2019-10-12"]]

def format_date(date_object):
    date_formatted = datetime.strftime(date_object, "%Y-%m-%dT00:00:00Z")
    return date_formatted


def generate_params(start, end):
    params = {"start_date": format_date(start), "end_date": format_date(end)}
    return params


def send_request(url, params):
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code != 200:
        raise RuntimeError(
            "failedRequest",
            "ERROR, {} code received from {}: {}".format(
                resp.status_code, url, resp.text
            ),
        )
    return resp.json()


def get_park_information(park_id, params):
    url = "{}{}{}".format(BASE_URL, AVAILABILITY_ENDPOINT, park_id)
    return send_request(url, params)


def get_name_of_site(park_id):
    url = "{}{}{}".format(BASE_URL, MAIN_PAGE_ENDPOINT, park_id)
    resp = send_request(url, {})
    return resp["campground"]["facility_name"]


def get_num_available_sites(resp, start_date, end_date):
    maximum = resp["count"]
    num_available = 0
    num_days = (end_date - start_date).days
    dates = [end_date - timedelta(days=i) for i in range(1, num_days + 1)]
    dates = set(format_date(i) for i in dates)
    for site in resp["campsites"].values():
        available = bool(len(site["availabilities"]))
        for date, status in site["availabilities"].items():
            if date not in dates:
                continue
            if status != "Available":
                available = False
                break
        if available:
            num_available += 1
    return num_available, maximum


def valid_date(s):
    try:
        return datetime.strptime(s, INPUT_DATE_FORMAT)
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def main(parks):
    client = Client(account_sid, auth_token)
    availabilities = False
    while(1):
        for dates in desired_weekends:
            availible_sites = []
            start = dates[0]
            end = dates[1]
            for park_id in parks:
                params = generate_params(valid_date(start), valid_date(end))
                park_information = get_park_information(park_id, params)
                name_of_site = get_name_of_site(park_id)
                current, maximum = get_num_available_sites(
                    park_information, valid_date(start), valid_date(end)
                )
                if current:
                    availabilities = True
                    availible_sites.append(name_of_site)
                    if availabilities:
                        url = "https://www.recreation.gov/camping/campgrounds/"+str(desired_sites[0])+"/availability"
                        message = client.messages \
                                .create(
                                    body="Available: " + availible_sites[0] + ": " + url + " from " + start + " to " + end,
                                    from_='+14132878694',
                                    to='+14133357767'
                        )
                        print( message.sid )
                        print("Available: " + availible_sites[0] + ": " + url)
                        return


if __name__ == "__main__":
    try:
        main(desired_sites)
    except Exception:
        print("Something went wrong")
        raise
