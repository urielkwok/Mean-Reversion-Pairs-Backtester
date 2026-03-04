import numpy as np
from statsmodels.tsa.stattools import adfuller as adf


def adf_test(series: np.ndarray) -> bool:
    """
    Requires: Nothing
    Modifies: Nothing
    Returns: True if series is stationary, False otherwise
    """
    result = adf(series)
    print(f"Raw ADF: {result[0]:.4f}, p-value: {result[1]:.4f}")
    if result[1] < 0.05:
        return True
    else:
        return False
