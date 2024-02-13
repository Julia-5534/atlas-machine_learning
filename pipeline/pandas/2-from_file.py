#!/usr/bin/env python3
"""Task 2"""

import pandas as pd


def from_file(filename, delimiter):
    """Loads data from a file as a pd.DataFrame"""
    # Load the data from the file
    df = pd.read_csv(filename, delimiter=delimiter)

    return df
