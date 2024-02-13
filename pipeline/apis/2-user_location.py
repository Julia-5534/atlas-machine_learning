#!/usr/bin/env python3
"""Task 2"""

import requests
import sys
from datetime import datetime, timedelta


def user_location(url):
    """
    Prints the location of a GitHub user.

    Args:
        url (str): The GitHub API URL for the user.

    If the user doesn't exist, prints "Not found".
    If the status code is 403, prints "Reset in X min" where X is the
    number of minutes from now and the value of 'X-Ratelimit-Reset'.
    Otherwise, prints the user's location.
    """
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_timestamp = response.headers.get('X-Ratelimit-Reset')
        reset_time = datetime.fromtimestamp(int(reset_timestamp))
        now = datetime.now()
        difference = reset_time - now
        print(f"Reset in {difference.seconds // 60} min")
    else:
        location = response.json().get('location')
        print(location)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        user_location(sys.argv[1])
