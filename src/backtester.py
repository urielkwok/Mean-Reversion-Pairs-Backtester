import numpy as np
import pandas as pd


def get_positions(df: pd.DataFrame) -> None:
    """
    Requires: z-scores and adf p-values calculated in stock_df
    Modifies: stock_df
    Effects: Creates positions for each z-score
    """
    df["is_stationary"] = df["adf_p_value"] < 0.05
    df["signal"] = 0
    df.loc[(df["z-score"] < -2) & (df["is_stationary"]), "signal"] = 1
    df.loc[(df["z-score"] > 2) & (df["is_stationary"]), "signal"] = -1
    df["position"] = df["signal"].replace(0, np.nan).ffill().fillna(0)
    df.loc[df["z-score"].abs() < 0.5, "position"] = 0
    df["spy_position"] = 1


def cum_returns(df: pd.DataFrame, stock_1: str, stock_2: str, beta: pd.Series, WINDOW: int) -> pd.Series:
    """
    Requires: Values and position are columns in stock_df
    Modifies: Nothing
    Effects: Calculates total returns
    """
    commission_cost = 0.0005
    stock_1_change = df[stock_1].diff()
    stock_2_change = df[stock_2].diff()
    pnl = df["position"].shift(1) * (stock_2_change - beta.shift(1) * stock_1_change)
    capital_required = df[stock_2] + (beta.abs() * df[stock_1])
    daily_returns = (pnl / capital_required).fillna(0)
    trade_made = df["position"].diff().fillna(0) != 0
    daily_returns.loc[trade_made] -= commission_cost
    daily_returns = daily_returns[WINDOW:]
    return daily_returns.cumsum()


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
    annual_returns = total_returns / years
    print(f"annualized returns: {annual_returns:.2%}")
    wealth_index = cumulative_returns + 1
    previous_peak = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peak) / previous_peak
    max_drawdown = drawdowns.min()
    print(f"max drawdown: {max_drawdown:.2%}")
