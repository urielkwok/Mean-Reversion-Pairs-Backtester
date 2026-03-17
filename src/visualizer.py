import matplotlib.pyplot as plt
import pandas as pd


def plot_values(df: pd.DataFrame, window: int) -> None:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Plot z-score and returns vs time
    """
    z_values = df["z-score"].dropna().iloc[window:]
    returns = df["cum_returns"].dropna()
    spy_returns = df["cum_SPY"].dropna()
    spread = df["spread"].dropna().iloc[window:]
    figure, axes = plt.subplots(3, 1, figsize=(9, 7))
    axes[0].plot(spread)
    axes[0].set_title("Spread vs Time")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Spread")
    axes[1].plot(z_values)
    axes[1].set_title("Z-Score vs Time")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Z-Scores")
    axes[2].plot(returns * 100, label="returns")
    axes[2].plot(spy_returns * 100, label="SPY_returns")
    axes[2].set_title("Returns vs Time")
    axes[2].set_xlabel("Time")
    axes[2].set_ylabel("Returns (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("data.png")
