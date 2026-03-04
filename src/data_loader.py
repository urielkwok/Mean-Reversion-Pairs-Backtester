import yfinance as yf
import pandas as pd
from datetime import datetime

START_YEARS_AGO = 2
END_YEARS_AGO = 0


def get_dates():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Returns correctly formatted start and end dates.
    """
    today = datetime.today()
    start_date = (today.replace(year=today.year - START_YEARS_AGO))
    modified_start_date = start_date.strftime("%Y-%m-%d")
    end_date = (today.replace(year=today.year - END_YEARS_AGO))
    modified_end_date = end_date.strftime("%Y-%m-%d")

    return modified_start_date, modified_end_date


def get_data(stock_1: str, stock_2: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Requires: Valid tickers, dates formatted as 'YYYY-MM-DD'.
    Modifies: Nothing
    Effects: Returns a DataFrame containing price data.
    """
    stock_df = yf.download([stock_1, stock_2, "SPY"], start_date, end_date)
    stock_df = stock_df["Close"].copy()

    return stock_df
