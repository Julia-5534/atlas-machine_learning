#!/usr/bin/env python3
"""Task 1"""

import requests


def sentientPlanets():
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()
        for species in data['results']:
            if 'sentient' in species[
                'classification'].lower() or 'sentient' in species[
                    'designation'].lower():
                if species['homeworld'] is not None:
                    planet_response = requests.get(species['homeworld'])
                    planet_data = planet_response.json()
                    planets.append(planet_data['name'])
        url = data['next']

    return planets
