import matplotlib.pyplot as plt
import pandas as pd


def plot_values(df: pd.DataFrame) -> None:
    """
    Requires: Nothing
    Modifies: Nothing
    Effects: Plot z-score and returns vs time
    """
    z_values = df["z-score"].dropna()
    returns = df["cum_returns"].dropna()
    spy_returns = df["cum_SPY"].dropna()
    figure, axes = plt.subplots(2, 1)
    axes[0].plot(z_values)
    axes[0].set_title("Z-Values vs Time")
    axes[0].set_xlabel("Time")
    axes[0].set_ylabel("Z-Values")
    axes[1].plot(returns * 100, label="returns (%)")
    axes[1].plot(spy_returns * 100, label="spy_returns (%)")
    axes[1].set_title("Returns vs Time")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Returns")
    plt.legend()
    plt.tight_layout()
    plt.savefig("data.png")
