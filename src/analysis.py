import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as sm


def rolling_adf_test(spread: pd.Series, WINDOW: int) -> pd.Series:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Returns series of p-values for each date
    """
    def get_p_value(x):
        if len(x) < WINDOW or np.isnan(x).any():
            return np.nan
        return sm.adfuller(x)[1]
    return spread.rolling(WINDOW).apply(get_p_value)


def rolling_beta(df: pd.DataFrame, stock_1: str, stock_2: str, window) -> pd.Series:
    """
    Requires: Both series contain rolling stock data
    Modifies: Nothing
    Effects: Calculates a rolling beta
    """
    rolling_cov = df[stock_1].rolling(window).cov(df[stock_2])
    rolling_var = df[stock_1].rolling(window).var()
    rolling_beta = rolling_cov / rolling_var
    return rolling_beta


def rolling_z_score(series: pd.Series, window: int) -> pd.Series:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Rolling z-score for each entry
    """
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()
    return (series - rolling_mean) / rolling_std
