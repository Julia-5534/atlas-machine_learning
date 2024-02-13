#!/usr/bin/env python3
"""Task 4"""

import requests
from collections import Counter


def fetch_and_display_launches():
    """Fetch and display sorted launches"""
    SPACE_LAUNCH_API = 'https://api.spacexdata.com/v5/launches'
    SPACE_ROCKET_API = 'https://api.spacexdata.com/v4/rockets'

    rocket_catalogue = {}

    # Retrieve all launched rockets from SPACE_LAUNCH_API
    space_launch_resp = requests.get(SPACE_LAUNCH_API)
    space_launch_data = space_launch_resp.json()
    space_rocket_ids = [rocket['rocket'] for rocket in space_launch_data]

    # Retrieve rocket_ids, rocket_names from SPACE_ROCKET_API
    space_rocket_resp = requests.get(SPACE_ROCKET_API)
    space_rocket_data = space_rocket_resp.json()
    space_rocket_identifiers = [rocket['id'] for rocket in space_rocket_data]
    space_rocket_monikers = [rocket['name'] for rocket in space_rocket_data]

    # Construct a dictionary of rocket_ids and rocket_names
    rocket_catalogue = dict(zip(
        space_rocket_identifiers,
        space_rocket_monikers))

    # Count and sort the launched rockets
    launch_tally = dict(sorted(Counter(space_rocket_ids).items(),
                               key=lambda x: x[1], reverse=True))

    # Replace keys in launch_tally with the appropriate rocket names
    final_tally = {rocket_catalogue[
        key]: value for key, value in launch_tally.items()}

    sorted_tally = sorted(final_tally.items(), key=lambda x: (-x[1], x[0]))

    for i in range(len(sorted_tally)):
        print(sorted_tally[i][0] + ': ' + str(sorted_tally[i][1]))


if __name__ == '__main__':
    fetch_and_display_launches()
