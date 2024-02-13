#!/usr/bin/env python3
"""Task 2"""

import requests
import sys
from datetime import datetime, timedelta


def get_location(url):
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        if json['location']:
            print(json['location'])
        else:
            print("Not found")
    elif response.status_code == 403:
        reset_timestamp = response.headers.get('X-Ratelimit-Reset')
        reset_time = datetime.fromtimestamp(int(reset_timestamp))
        now = datetime.now()
        difference = reset_time - now
        print(f"Reset in {difference.seconds // 60} min")
    else:
        print("Not found")


if __name__ == '__main__':
    get_location(sys.argv[1])
