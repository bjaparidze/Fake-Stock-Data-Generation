import numpy as np


def add_missing_values(missing_prob, collection):
    """
    Adds missing values to a given collection randomly given the missing probability.
    If the column contains floating point values, np.nan is added,
    if the column contains ints, then —— -9999
    """
    length = len(collection)

    # Generate indices for introducing missing values based on missing probability
    missing_indices = np.random.choice(
        length, size=int(missing_prob * length), replace=False
    )

    # Loop through the selected indices and introduce missing values
    for idx in missing_indices:
        try:
            collection[idx] = np.nan
        except ValueError:
            collection[idx] = -9999
