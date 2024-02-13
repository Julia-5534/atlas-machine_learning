#!/usr/bin/env python3
"""Task 3"""

import requests
import datetime
import pytz


def get_first_launch():
    """Displays the First Launch"""
    response = requests.get('https://api.spacexdata.com/v4/launches')
    launches = response.json()

    # Get the specific launch
    for launch in launches:
        if launch['name'] == 'Galaxy 33 (15R) & 34 (12R)':
            first_launch = launch
            break

    # Get the required information
    launch_name = first_launch['name']
    date_unix = first_launch['date_unix']
    rocket_id = first_launch['rocket']
    launchpad_id = first_launch['launchpad']

    # Convert the date from unix to local time
    date_local = datetime.datetime.fromtimestamp(
        date_unix,
        tz=pytz.timezone('US/Eastern'))

    # Get the rocket name
    rocket_response = requests.get(
        'https://api.spacexdata.com/v4/rockets/{}'.format(rocket_id))
    rocket_name = rocket_response.json()['name']

    # Get the launchpad name and locality
    launchpad_response = requests.get(
        'https://api.spacexdata.com/v4/launchpads/{}'.format(launchpad_id))
    launchpad_name = launchpad_response.json()['name']
    launchpad_locality = launchpad_response.json()['locality']

    # Format the output
    output = "{} ({}) {} - {} ({})".format(
        launch_name,
        date_local.isoformat(),
        rocket_name,
        launchpad_name,
        launchpad_locality)

    return output


if __name__ == '__main__':
    print(get_first_launch())
