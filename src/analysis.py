import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as sm


def rolling_adf_test(df: pd.DataFrame, stock_1: str, stock_2: str, window: int) -> pd.Series:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Returns series of p-values for each date
    """
    beta = rolling_beta(df, stock_1, stock_2, window)
    spread = df[stock_2] - (beta * df[stock_1])

    def get_p_value(x):
        if len(x) < window or np.isnan(x).any():
            return np.nan
        return sm.adfuller(x)[1]
    return spread.rolling(window).apply(get_p_value)


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


def rolling_z_score(spread: pd.Series, window: int) -> pd.Series:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Rolling z-score for each entry
    """
    rolling_mean = spread.rolling(window).mean()
    rolling_std = spread.rolling(window).std()
    return (spread - rolling_mean) / rolling_std
