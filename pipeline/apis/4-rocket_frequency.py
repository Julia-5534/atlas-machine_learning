#!/usr/bin/env python3
"""Task 4"""

import requests
from collections import Counter

launch_url = 'https://api.spacexdata.com/v3/launches'
rocket_url = 'https://api.spacexdata.com/v3/rockets'


def get_launches_per_rocket():
    """Displays the number of launches per rocket"""
    # Get the launch and rocket data
    launches = requests.get(launch_url).json()
    rockets = requests.get(rocket_url).json()

    # Create a dictionary to store the rocket names
    rocket_names = {
        rocket['rocket_id']: rocket['rocket_name'] for rocket in rockets}

    # Get the rocket id for each launch and count the number of launches
    launched_rockets = [
        launch['rocket']['rocket_id'] for launch in launches]
    launches_per_rocket = Counter(launched_rockets)

    # Replace the rocket ids with the rocket names and sort the result
    rockets_and_launches = {
        rocket_names[
            rocket_id]: count for rocket_id,
        count in launches_per_rocket.items()}
    sorted_rockets_and_launches = sorted(
        rockets_and_launches.items(), key=lambda x: (-x[1], x[0]))

    return sorted_rockets_and_launches


if __name__ == '__main__':
    for rocket_name, num_launches in get_launches_per_rocket():
        print("{}: {}".format(rocket_name, num_launches))
