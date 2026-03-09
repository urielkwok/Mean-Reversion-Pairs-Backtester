import matplotlib.pyplot as plt
import pandas as pd


def plot_values(stock_df: pd.DataFrame) -> None:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Plot z-score and returns vs time
    """
    z_values = stock_df["z-score"].dropna()
    returns = stock_df["cumulative_returns"].dropna()
    spy_returns = stock_df["cumulative_SPY"].dropna()
    figure, axes = plt.subplots(2, 1)
    axes[0].plot(z_values)
    axes[0].set_title("Z-Values vs Time")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Z-Values")
    axes[1].plot(returns, label="returns")
    axes[1].plot(spy_returns, label="spy_returns")
    axes[1].set_title("Returns vs Time")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Returns")
    plt.legend()
    plt.tight_layout()
    plt.savefig("data.png")
