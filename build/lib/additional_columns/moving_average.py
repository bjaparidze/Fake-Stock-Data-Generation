import numpy as np


class MovingAverage:
    @staticmethod
    def calculate_moving_average(close_prices, window_size):
        # calculate the moving average
        weights = np.repeat(1.0, window_size) / window_size
        moving_average = np.convolve(close_prices, weights, "valid")

        # pad the resulting array by (window_size - 1) to retain the original length
        # and return the resulting array
        return np.concatenate(
            (np.full(window_size - 1, np.nan), moving_average), axis=None
        )
