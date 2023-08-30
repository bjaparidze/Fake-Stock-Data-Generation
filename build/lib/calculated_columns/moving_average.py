import numpy as np


def calculate_moving_average(close_prices, window_size):
    """
    Calculates Simple Moving Average values given close price values and a window size.
    Returns a numpy array
    """
    # calculate the moving average
    weights = np.repeat(1.0, window_size) / window_size
    moving_average = np.convolve(close_prices, weights, "valid")

    # pad the resulting array by (window_size - 1) to retain the original length
    # and return the resulting array
    return np.concatenate(
        (np.full(window_size - 1, np.nan), moving_average), axis=None
    )
