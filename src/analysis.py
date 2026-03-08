import numpy as np
import pandas as pd
import statsmodels.tsa.stattools as sm


def adf_test(series: np.NDArray) -> bool:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: True if series is stationary, False otherwise
    """
    result = sm.adfuller(series)
    print(f"Raw ADF: {result[0]:.4f}, p-value: {result[1]:.4f}")
    if result[1] < 0.05:
        return True
    else:
        return False


def OLS_regression(ind_stock: np.NDArray, dep_stock: np.NDArray) -> tuple[float, float]:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: Alpha and Beta values for the two variables
    """
    x = sm.add_constant(ind_stock)
    y = dep_stock
    regression = sm.OLS(y, x).fit()
    alpha = regression.params.iloc[0]
    beta = regression.params.iloc[1]
    return alpha, beta


def rolling_z_score(series: pd.Series, window: int) -> np.NDArray[np.float64]:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: Rolling z-score for each entry
    """
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()
    return (series - rolling_mean) / rolling_std
