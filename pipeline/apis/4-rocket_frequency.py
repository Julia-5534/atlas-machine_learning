#!/usr/bin/env python3
"""Task 4"""

import requests
from collections import defaultdict


def get_launches():
    response = requests.get('https://api.spacexdata.com/v3/launches')
    data = response.json()
    return data


def count_launches(launches):
    """Counts Launches"""
    count_dict = defaultdict(int)
    for launch in launches:
        rocket_name = launch['rocket']['rocket_name']
        count_dict[rocket_name] += 1
    return count_dict


def print_sorted_counts(count_dict):
    """Prints Sorted Counts"""
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for rocket, count in sorted_counts:
        print("{}: {}".format(rocket, count))

if __name__ == '__main__':
    launches = get_launches()
    count_dict = count_launches(launches)
    print_sorted_counts(count_dict)
