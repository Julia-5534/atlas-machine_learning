#!/usr/bin/env python3
"""Task 12"""

import pandas as pd
from_file = __import__('2-from_file').from_file


df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Index the DataFrames on the Timestamp columns
df1.set_index('Timestamp', inplace=True)
df2.set_index('Timestamp', inplace=True)

# Concatenate the bitstamp and coinbase tables from
# timestamps 1417411980 to 1417417980, inclusive
df1 = df1.loc[1417411980:1417417980]
df2 = df2.loc[1417411980:1417417980]

# Add keys to the data labeled bitstamp and coinbase respectively
df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

# Swap the levels of the MultiIndex to make 'Timestamp' the first level
df = df.swaplevel()

# Sort the index in chronological order
df.sort_index(inplace=True)

print(df)
