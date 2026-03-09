import numpy as np
import pandas as pd


def get_positions(stock_df: pd.DataFrame) -> None:
    """
    Requires: z-scores calculated in stock_df
    Modifies: stock_df
    Effects: Creates positions for each z-score
    """
    stock_df["signal"] = 0
    stock_df.loc[stock_df["z-score"] < -2, "signal"] = 1
    stock_df.loc[stock_df["z-score"] > 2, "signal"] = -1
    stock_df["position"] = stock_df["signal"].replace(0, np.nan).ffill().fillna(0)
    stock_df.loc[stock_df["z-score"].abs() < 0.5, "position"] = 0
    stock_df["spy_position"] = 1


def cumulative_returns(values: pd.Series, position: pd.Series) -> pd.Series:
    """
    Requires: Values and position are columns in stock_df
    Modifies: Nothing
    Effects: Calculates total returns
    """
    pct_change = values.pct_change()
    returns = position.shift(1) * pct_change
    returns = returns.fillna(0)
    cumulative_returns = (1 + returns).cumprod() - 1
    return cumulative_returns
