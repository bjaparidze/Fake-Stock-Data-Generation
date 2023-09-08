import math
import string
import re
import random
import pandas as pd
from faker import Faker
from faker.providers import BaseProvider
from utilities.missing_values import add_missing_values


class NamesAndTickers(BaseProvider):
    """
    Custom Provider of company names and tickers for python's faker library
    """

    def generate_names_and_tickers(
        self, time_period_in_days: int, num_rows: int, **kwargs
    ) -> pd.DataFrame:
        """
        Generates fake company names and their corresponding tickers.
        Names repeat 'time_period_in_days' times until desired number of rows is reached.
        Returns pandas dataframe.
        """
        fake = Faker()
        companies = []
        tickers = []
        num_of_repeated_comps = math.ceil(num_rows / time_period_in_days)

        for _ in range(num_of_repeated_comps):
            # Generate fake company name
            company_name = fake.company()

            # Generate fake ticker
            initials = "".join(word[0] for word in re.split(r"[ -]", company_name))
            random_chars = "".join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(3)
            )
            ticker_name = initials.upper() + random_chars
            companies.append(company_name)
            tickers.append(ticker_name)

        # Duplicate company names and tickers based on time_period_in_days
        companies = [
            company for company in companies for _ in range(time_period_in_days)
        ]
        tickers = [ticker for ticker in tickers for _ in range(time_period_in_days)]

        data = {"Company": companies[:num_rows], "Ticker": tickers[:num_rows]}

        # Add missing values
        for column, missing_prob in kwargs.items():
            add_missing_values(missing_prob, data[column])

        return pd.DataFrame(data)
