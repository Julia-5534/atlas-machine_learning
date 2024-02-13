#!/usr/bin/env python3
"""Task 0"""

import pandas as pd
import string


def from_numpy(array):
    """Ceates a pd.DataFrame from a np.ndarray"""
    # Create a list of uppercase letters in the alphabet
    labels = list(string.ascii_uppercase)

    # Create a DataFrame from the ndarray
    df = pd.DataFrame(array)

    # Assign the column labels
    df.columns = labels[:len(df.columns)]

    return df
