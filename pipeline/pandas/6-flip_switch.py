#!/usr/bin/env python3
"""Task 6"""

import pandas as pd
from_file = __import__('2-from_file').from_file


df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Transpose the DataFrame
df = df.transpose()

# Convert the index to datetime and sort in reverse chronological order
df.columns = pd.to_datetime(df.columns)
df = df.sort_index(axis=1, ascending=False)

print(df.tail(8))
