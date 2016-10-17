#Chris Gala 64338761

import mapquest_input
import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Fmjtd%7Cluu8216zng%2Cal%3Do5-94251y'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route'

def build_search_url(location_list: list) -> str:
    query_parameters = [('from', location_list[0])]

    for location in location_list[1:]:
        query_parameters.append(('to', location))

    return BASE_MAPQUEST_URL + '?key=' + MAPQUEST_API_KEY + '&' + urllib.parse.urlencode(query_parameters)

def get_information(url: str) -> 'json':

    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

locations = mapquest_input.get_locations()
search = build_search_url(locations)
result = get_information(search)
