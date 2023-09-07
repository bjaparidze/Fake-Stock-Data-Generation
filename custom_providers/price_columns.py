import numpy as np
import pandas as pd
from faker.providers import BaseProvider
from prices_with_gbm.gen_gbm_close_prices import generate_close_prices


class PriceColumns(BaseProvider):
    """
    Custom provider of price and volume values for python's faker library
    """

    def generate_prices(
        self, num_of_companies: int, sample_size: int, num_of_days: int
    ) -> pd.DataFrame:
        """
        Generates Open, Close, High and Low Prices and Volume columns for a given number of companies over given number of days.
        To generate missing values, pass a dictionary as a parameter with column names as keys and probabilities as values.
        Returns a pandas dataframe
        """

        close_prices = generate_close_prices(
            num_of_companies=num_of_companies,
            sample_size=sample_size,
            num_of_days=num_of_days,
        )

        close_prices = np.clip(close_prices, a_min=1, a_max=1000)

        open_prices = np.empty_like(close_prices)
        for i in range(close_prices.shape[1]):
            for j in range(1, close_prices.shape[0]):
                open_prices[j, i] = close_prices[j-1, i] + np.random.normal(0, 0.5)

        # drop the first row from close_prices and open_prices arrays and flatten them
        flattened_close_prices = close_prices[1:].flatten()
        df = pd.DataFrame({"Close Price": flattened_close_prices})

        flattened_open_prices = open_prices[1:].flatten()
        df['Open Price'] = flattened_open_prices

        low_prices = np.minimum(df['Open Price'], df['Close Price'].to_numpy()) - np.random.uniform(0, 100, len(df))
        low_prices = np.clip(low_prices, a_min=1, a_max=1100)

        high_prices = np.maximum(df['Open Price'], df['Close Price'].to_numpy()) + np.random.uniform(0, 100, len(df))
        high_prices = np.clip(high_prices, a_min=1, a_max=1100)

        df['High Price'] = high_prices
        df['Low Price'] = low_prices

        df['Volume'] = np.random.randint(10_000, 1_000_000, len(df))

        return df
