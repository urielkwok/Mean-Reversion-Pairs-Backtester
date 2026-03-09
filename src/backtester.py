import numpy as np


def backtest(stock_df):
    stock_df["signal"] = 0
    stock_df.loc[stock_df["z-score"] < -2, "signal"] = 1
    stock_df.loc[stock_df["z-score"] > 2, "signal"] = -1
    stock_df["position"] = stock_df["signal"].replace(0, np.nan).ffill().fillna(0)
    stock_df.loc[stock_df["z-score"].abs() < 0.5, "position"] = 0
    stock_df["pct_change"] = stock_df["spread"].pct_change()
    stock_df["returns"] = stock_df["position"].shift(1) * stock_df["pct_change"]
    stock_df["total_returns"] = (1 + stock_df["returns"]).cumprod()
    print(f"{stock_df["total_returns"]:.2f}")
