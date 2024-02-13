#!/usr/bin/env python3
"""Task 14"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import for changing date format
import matplotlib.ticker as ticker  # Import for changing y-axis notation
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Drop all data before Midnight January 1, 2017
df = df[(df['Timestamp'] >= 1483228800)]

# Remove Weighted_Price column
df.drop(columns=['Weighted_Price'], inplace=True)

# Set missing values in Close column to previous row value
df['Close'].fillna(method='ffill', inplace=True)

# Set missing values in High, Low, Open columns to Close value
df['High'].fillna(df['Close'], inplace=True)
df['Low'].fillna(df['Close'], inplace=True)
df['Open'].fillna(df['Close'], inplace=True)

# Set missing values in Volume_(BTC) and Volume_(Currency) to 0
df['Volume_(BTC)'].fillna(0, inplace=True)
df['Volume_(Currency)'].fillna(0, inplace=True)

# Rename column Timestamp to Data
df.rename(columns={'Timestamp': 'Date'}, inplace=True)

# Convert 'Timestamp' values to Date 'values' and index
df['Date'] = pd.to_datetime(df['Date'], unit='s')
df.set_index('Date', inplace=True)

# Clean up so I only have daily data (1440 minutes per day)
df = df.iloc[::1440, :]

# Visualize
fig, ax = plt.subplots()  # Create a figure and axes

ax.plot(df.index, df['Open'], label='Open')
ax.plot(df.index, df['High'], label='High')
ax.plot(df.index, df['Low'], label='Low')
ax.plot(df.index, df['Close'], label='Close')
ax.plot(df.index, df['Volume_(BTC)'], label='Volume_(BTC)')
ax.plot(df.index, df['Volume_(Currency)'], label='Volume_(Currency)')

# Change date format on x-axis
date_format = mdates.DateFormatter('%Y-%m')
plt.gca().xaxis.set_major_formatter(date_format)

# Change y-axis notation
tick_format = ticker.StrMethodFormatter('{x:.0f}')
plt.gca().get_yaxis().set_major_formatter(tick_format)

plt.xlabel('Date')  # Label x-axis as 'Date'

plt.legend()
plt.show()
