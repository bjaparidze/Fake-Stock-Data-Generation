import numpy as np
import pandas as pd
from faker.providers import BaseProvider
from utilities.missing_values import add_missing_values


class PriceColumns(BaseProvider):
    """
    Custom provider of price and volume values for python's faker library
    """

    def generate_prices(self, num_rows: int, price_range: tuple, **missing_prob_dict) -> pd.DataFrame:
        """
        Generates Open, Close, High and Low Prices and Volume columns.
        To generate missing values, pass a dictionary as a parameter with column names as keys and probabilities as values.
        Returns a pandas dataframe
        """
        np.random.seed(42)

        # Normal distribution for gradual changes
        normal_fluctuations = np.random.normal(50, 10, num_rows)
        # Uniform distribution for occasional jumps
        uniform_jumps = np.random.uniform(-100, 100, num_rows)

        # Calculate cumulative sums for gradual and jump fluctuations
        cumulative_changes = normal_fluctuations + uniform_jumps
        cumulative_prices = price_range[0] + np.cumsum(cumulative_changes)
        # Clip prices to stay within the range
        clipped_prices = np.clip(cumulative_prices, price_range[0], price_range[1])

        # Generate distinct open and close prices
        # Also high and low prices
        open_prices = clipped_prices + np.random.uniform(-5, 5, num_rows)
        close_prices = clipped_prices - np.random.uniform(-5, 5, num_rows)
        high_prices = np.maximum(open_prices, close_prices) + np.random.uniform(0, 20)
        low_prices = np.minimum(open_prices, close_prices) - np.random.uniform(0, 20)

        # Generate random volume using NumPy
        volume = np.random.randint(10000, 1000000, num_rows)

        data = {
            "Open Price": open_prices,
            "Close Price": close_prices,
            "High Price": high_prices,
            "Low Price": low_prices,
            "Volume": volume,
        }

        # Add missing values
        for column, missing_prob in missing_prob_dict.items():
            add_missing_values(missing_prob, data[column])

        dataframe = pd.DataFrame(data)

        return dataframe
