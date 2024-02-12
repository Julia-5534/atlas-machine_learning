#!/usr/bin/env python3
"""Task 1"""

import pandas as pd


# Define the dictionary
data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Set the row labels
df.index = ['A', 'B', 'C', 'D']
