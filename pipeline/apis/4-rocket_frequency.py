#!/usr/bin/env python3
"""Task 4"""

import requests
from collections import defaultdict


def get_launches_per_rocket():
    """Displays the number of launches per rocket"""
    response = requests.get('https://api.spacexdata.com/v3/launches')
    launches = response.json()

    # Create a dictionary to store the number of launches per rocket
    launches_per_rocket = defaultdict(int)

    # Get the rocket id for each launch and
    # increment the count in the dictionary
    for launch in launches:
        rocket_id = launch['rocket']['rocket_id']
        launches_per_rocket[rocket_id] += 1

    # Get the rocket names
    rocket_names = {}
    for rocket_id in launches_per_rocket.keys():
        response = requests.get(
            f'https://api.spacexdata.com/v3/rockets/{rocket_id}')
        rocket_names[rocket_id] = response.json()['rocket_name']

    # Create a list of tuples (rocket name, number of launches)
    rockets_and_launches = [
        (rocket_names[id],
         launches_per_rocket[id]) for id in launches_per_rocket.keys()]

    # Sort the list by number of launches (descending) and rocket name (A to Z)
    sorted_rockets_and_launches = sorted(
        rockets_and_launches, key=lambda x: (-x[1], x[0]))

    return sorted_rockets_and_launches


if __name__ == '__main__':
    for rocket_name, num_launches in get_launches_per_rocket():
        print(f"{rocket_name}: {num_launches}")
