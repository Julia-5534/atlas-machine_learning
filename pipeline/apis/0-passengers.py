#!/usr/bin/env python3
"""Task 0"""

import requests


def availableShips(passengerCount):
    """Returns the list of ships that can hold a given number of passengers"""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()
        for ship in data['results']:
            try:
                if int(ship['passengers']) >= passengerCount:
                    ships.append(ship['name'])
            except ValueError:
                pass
        url = data['next']

    return ships
