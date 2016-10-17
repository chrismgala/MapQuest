#Chris Gala 64338761

import mapquest_output
import mapquest_api_connect

def get_locations() -> list:
    number_of_locations = int(input())
    location_list = []

    for number in range(number_of_locations):
        location = input()
        location_list.append(location)

    return location_list

def get_outputs() -> list:
    number_of_direction_outputs = int(input())
    output_list = []

    for number in range(number_of_direction_outputs):
        output = input()
        output_list.append(output.upper())

    return output_list

def run_output(mapquest_outputs: ['mapquest_output'], outputs: ['output'], json_result: 'json'):
    if 'STEPS' in outputs:
        mapquest_outputs[0].print(json_result)
    if 'TOTALDISTANCE' in outputs:
        mapquest_outputs[1].print(json_result)
    if 'TOTALTIME' in outputs:
        mapquest_outputs[2].print(json_result)        
    if 'LATLONG' in outputs:
        mapquest_outputs[3].print(json_result)
    print('\n' + 'Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

if __name__ == '__main__':
    outputs = get_outputs()
    run_output([mapquest_output.Steps(), mapquest_output.Distance(), mapquest_output.Time(), mapquest_output.LatLong()], outputs, mapquest_api_connect.result)
