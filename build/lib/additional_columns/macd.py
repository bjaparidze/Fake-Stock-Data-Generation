import pandas as pd


class MACD:
    @staticmethod
    def calculate_macd(data: pd.DataFrame, close_price_col: str):
        # Calculate the 12-period and 26-period EMA
        data["EMA12"] = data[close_price_col].ewm(span=12, adjust=False).mean()
        data["EMA26"] = data[close_price_col].ewm(span=26, adjust=False).mean()

        # Calculate the MACD line
        data["MACD"] = data["EMA12"] - data["EMA26"]

        data.drop(["EMA12", "EMA26"], axis=1)

        # Calculate the MACD single line (9-period EMA of the MACD)
        data["Signal_Line"] = data["MACD"].ewm(span=9, adjust=False).mean()
