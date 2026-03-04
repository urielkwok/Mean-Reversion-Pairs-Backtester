import numpy as np
from statsmodels.tsa.stattools import adfuller as adf


def adf_test(series: np.ndarray) -> str:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: Dict containing Raw ADF and p-value for the series.
    """
    result = adf(series)
    return f"Raw ADF: {result[0]:.4f}, p-value: {result[1]:.4f}"
