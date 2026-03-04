import numpy as np
from statsmodels.tsa.stattools import adfuller as adf


def adf_test(series: np.NDArray) -> bool:
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


def z_score(series: np.ndarray) -> np.NDArray[np.float64]:
    """
    Requires; Nothing
    Modifies: Nothing
    Returns: z-score for each entry in the series
    """
    return (series - np.mean(series)) / np.std(series)
