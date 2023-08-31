import numpy as np
import pandas as pd


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


def add_missing_values_to_df(df: pd.DataFrame, **missing_prob_dict):
    """
    Adds missing values to a given pandas dataframe.
    User has to pass a dictionary with column names as keys and probability of missing values as values.
    """
    num_rows = len(df)

    for column, missing_prob in missing_prob_dict.items():
        missing_indices = np.random.choice(
            num_rows, size=int(missing_prob * num_rows), replace=False
        )
        # missing_indices = tuple(missing_indices)
        try:
            df.loc[missing_indices, column] = np.nan
        except ValueError:
            df.loc[missing_indices, column] = -9999