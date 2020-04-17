import recreation_gov.api.park_search_api as test

print(test.park_search_request("yosemite").get('inventory_suggestions'))