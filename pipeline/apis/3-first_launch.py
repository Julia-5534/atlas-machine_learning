#!/usr/bin/env python3
"""Task 3"""

import requests
import datetime


def get_first_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches')
    launches = response.json()

    # Sort the launches by date_unix
    sorted_launches = sorted(launches, key=lambda k: k['date_unix'])

    # Get the first launch
    first_launch = sorted_launches[0]

    # Get the required information
    launch_name = first_launch['name']
    date_unix = first_launch['date_unix']
    rocket_id = first_launch['rocket']
    launchpad_id = first_launch['launchpad']

    # Convert the date from unix to local time
    date_local = datetime.datetime.fromtimestamp(date_unix)

    # Get the rocket name
    rocket_response = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
    rocket_name = rocket_response.json()['name']

    # Get the launchpad name and locality
    launchpad_response = requests.get(f'https://api.spacexdata.com/v4/launchpads/{launchpad_id}')
    launchpad_name = launchpad_response.json()['name']
    launchpad_locality = launchpad_response.json()['locality']

    # Format the output
    output = f"{launch_name} ({date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
    
    return output

if __name__ == '__main__':
    print(get_first_launch())
