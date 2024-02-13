#!/usr/bin/env python3
"""Task 4"""

import requests
from collections import Counter


def fetch_and_display_launches():
    """
    Fetches launch and rocket data from SpaceX API,
    counts the number of launches for each rocket,
    sorts the rockets by the number of launches, and
    displays the result.
    """
    # URLs for SpaceX API endpoints
    SPACE_LAUNCH_API = 'https://api.spacexdata.com/v5/launches'
    SPACE_ROCKET_API = 'https://api.spacexdata.com/v4/rockets'

    # Dictionary to store rocket names
    rocket_catalogue = {}

    # Fetch all launched rockets from SpaceX API
    space_launch_resp = requests.get(SPACE_LAUNCH_API)
    space_launch_data = space_launch_resp.json()
    # Extract rocket IDs from the launch data
    space_rocket_ids = [rocket['rocket'] for rocket in space_launch_data]

    # Fetch rocket data from SpaceX API
    space_rocket_resp = requests.get(SPACE_ROCKET_API)
    space_rocket_data = space_rocket_resp.json()
    # Extract rocket IDs and names from the rocket data
    space_rocket_identifiers = [rocket['id'] for rocket in space_rocket_data]
    space_rocket_monikers = [rocket['name'] for rocket in space_rocket_data]

    # Create a dictionary mapping rocket IDs to rocket names
    rocket_catalogue = dict(zip(
        space_rocket_identifiers,
        space_rocket_monikers))

    # Count the number of launches for each rocket and sort by count
    launch_tally = dict(
        sorted(Counter(space_rocket_ids).items(),
               key=lambda x: x[1],
               reverse=True))

    # Replace rocket IDs with rocket names in the launch tally
    final_tally = {
        rocket_catalogue[key]: value for key,
        value in launch_tally.items()}

    # Sort the final tally by number of launches (descending)
    # and rocket name (ascending)
    sorted_tally = sorted(
        final_tally.items(),
        key=lambda x: (-x[1], x[0]))

    # Print the sorted tally
    for i in range(len(sorted_tally)):
        print(sorted_tally[i][0] + ': ' + str(sorted_tally[i][1]))


if __name__ == '__main__':
    fetch_and_display_launches()
