import math
import pandas as pd
import numpy as np
from faker.providers import BaseProvider
from utilities.missing_values import add_missing_values


class Sectors(BaseProvider):
    """
    Custom Provider of sector names for python's faker library
    """

    def generate_sectors(
        self,
        num_rows: int,
        time_period_in_days: int,
        add_nan_values=False,
        missing_prob=None,
    ) -> pd.DataFrame:
        """
        Generates fake company sectors.
        Sectors repeat 'time_period_in_days' times until desired number of rows is reached.
        Returns pandas dataframe.
        """
        num_of_repeated_sectors = math.ceil(num_rows / time_period_in_days)

        # Define list of sectors
        sectors = ["Technology", "Finance", "Healthcare", "Energy", "Consumer Goods"]
        # Generate random sectors for each company
        company_sectors = np.random.choice(sectors, num_of_repeated_sectors)

        # Duplicate company names and tickers based on time_period_in_days
        company_sectors = [
            sector for sector in company_sectors for _ in range(time_period_in_days)
        ]

        # Add missing values
        if add_nan_values:
            add_missing_values(missing_prob, company_sectors)

        data = {"Sector": company_sectors[:num_rows]}

        return pd.DataFrame(data)
