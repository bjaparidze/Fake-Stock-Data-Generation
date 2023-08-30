import math
import pandas as pd
from faker import Faker
from datetime import timedelta
from faker.providers import BaseProvider
from utilities.missing_values import add_missing_values


class Dates(BaseProvider):
    """
    Custom Provider of dates for python's faker library
    """

    def generate_dates(
        self,
        time_period_in_days: int,
        num_rows: int,
        add_nan_values=False,
        missing_prob=None,
    ) -> pd.DataFrame:
        """
        Generates fake sequential dates that repeat over the specified time period.
        ex.: generates 90 dates that increase by 1 day and repeats them until specified number of rows is reached in a dataframe.
        returns a pandas dataframe object.
        """
        fake = Faker()
        # Initial date
        initial_date = fake.date_this_year()

        # List to store generated dates
        distinct_dates = []

        # Generate sequential dates over a given time period
        for _ in range(time_period_in_days):
            distinct_dates.append(initial_date)
            initial_date += timedelta(days=1)

        # Calculate repetitions needed to fill desired rows
        repetitions = math.ceil(num_rows / time_period_in_days)

        # Multiply the distinct dates and trim the list
        date_list = distinct_dates * repetitions
        date_list = date_list[:num_rows]

        if add_nan_values:
            add_missing_values(missing_prob, date_list)

        data = {"Date": date_list}
        return pd.DataFrame(data)
