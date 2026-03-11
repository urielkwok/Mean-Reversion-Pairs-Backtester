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


def cumulative_returns(values: pd.Series, position: pd.Series, investment: pd.Series, rolling_window: int) -> pd.Series:
    """
    Requires: Values and position are columns in stock_df
    Modifies: Nothing
    Effects: Calculates total returns
    """
    change = values.diff()
    PnL = position.shift(1) * change
    returns = PnL / investment.ffill()
    returns = returns.fillna(0)
    returns = returns[rolling_window:]
    cumulative_returns = (1 + returns).cumprod() - 1
    return cumulative_returns


def get_measurements(cumulative_returns: pd.Series, rolling_window: int) -> None:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Calculates sharpe ratio using cumulative_returns.
    """
    cumulative_returns = cumulative_returns.iloc[rolling_window:]
    daily_returns = cumulative_returns.diff().fillna(0)
    sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)
    print(f"sharpe ratio: {sharpe_ratio:.4f}")
    total_returns = cumulative_returns.iloc[-1]
    days = cumulative_returns.shape[0]
    years = days / 252
    annual_returns = (1 + total_returns) ** (1 / years) - 1
    print(f"annualized returns: {annual_returns:.4f}")
    wealth_index = cumulative_returns + 1
    previous_peak = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peak) / previous_peak
    max_drawdown = drawdowns.min()
    print(f"max drawdown: {max_drawdown:.2%}")
