#Chris Gala 64338761

import mapquest_api_connect
import math

class Steps:
    def print(self, json_result: 'json') -> None:
        print()
        print('DIRECTIONS')
        for part in json_result['route']['legs']:
            for direction in part['maneuvers']:
                print(direction['narrative'])
    
class Distance:
    def print(self, json_result: 'json') -> None:
        print()
        miles = 0
        for part in json_result['route']['legs']:
            miles += part['distance']
        print('Total distance:', str(round(miles, 0)).strip(".0"), 'miles')

class Time:
    def print(self, json_result: 'json') -> None:
        print()
        minutes = 0
        seconds = 0
        for part in json_result['route']['legs']:
                minutes += int(part['formattedTime'].split(':')[1])
                seconds += int(part['formattedTime'].split(':')[2])
        minutes += (seconds / 60)
        print('Total time:', str(round(minutes, 0)).strip(".0"), 'minutes')

class LatLong:
    def print(self, json_result: 'json') -> None:
        print()
        for city in json_result['route']['locations']:
            if city['latLng']['lat'] > 0:
                print(round(city['latLng']['lat'], 2), 'N ', end='')
            if city['latLng']['lat'] < 0:
                print(round(abs(city['latLng']['lat']), 2), 'S ', end='')
            if city['latLng']['lng'] > 0:
                print(round(city['latLng']['lng'], 2), 'E')
            if city['latLng']['lng'] < 0:
                print(round(abs(city['latLng']['lng']), 2), 'W')
